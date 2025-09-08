from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from users.models import Follow


'''list all the post and even you can create new'''
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


'''retrive edit/delete/fetch post - only by owner'''
class PostDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user = self.request.user)
    
'''feed from the followed users'''
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following_set.values_list("following", flat=True)
        return Post.objects.filter(user__id__in=following_users).order_by("-created_at")
    


class PostUpdateView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request, post_id):
        #  Get the post
        post = get_object_or_404(Post, id=post_id)
        
        #  Check ownership
        if post.user != request.user:
            return Response({"error": "You can't edit this post"}, status=403)
        
        #  Update fields
        post.caption = request.data.get('caption', post.caption)
        if 'image' in request.data:
            post.image = request.data.get('image')
        
        #  Save post
        post.save()
        
        #  Return updated data
        serializer = PostSerializer(post)
        return Response(serializer.data, status=200)
