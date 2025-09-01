from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.authtoken.models import Token  # token ke liye import

class LoginView(APIView):
    def post(self, request):

        
        # Fetch data from request
        username = request.data.get('username')
        password = request.data.get('password')

        #  Fetch user from DB
        user = CustomUser.objects.filter(username=username).first()

        # Check if user exists
        if user is not None:
            # Check password
            if user.check_password(password):


                # For Generate token
                token, created = Token.objects.get_or_create(user=user)

                # Return success response with token
                return Response({
                    "message": "Login successful",
                    "token": token.key,
                    "username": user.username,
                    "email": user.email
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credentials are wrong"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Credentials are wrong"}, status=status.HTTP_400_BAD_REQUEST)
