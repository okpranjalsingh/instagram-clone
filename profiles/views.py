from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import ProfileSerializer

User = get_user_model()

# View & Update your own profile
class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


# View another user's profile
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs['user_id']
        return get_object_or_404(Profile, user__id=user_id)


# Follow another user
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        target_user.profile.followers.add(request.user)
        return Response({"message": f"You are now following {target_user.username}"}, status=200)


# Unfollow a user
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if target_user == request.user:
            return Response({"error": "You cannot unfollow yourself"}, status=400)

        target_user.profile.followers.remove(request.user)
        return Response({"message": f"You have unfollowed {target_user.username}"}, status=200)
