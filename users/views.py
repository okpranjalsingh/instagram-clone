from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"The account has been created successfully!"
            }, status= status.HTTP_201_CREATED)
            
        else:
            return Response (
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        

class LoginView(APIView):
    def post(self, request):
        # Fetch data from request
        email = request.data.get('email')
        password = request.data.get('password')
        #  Fetch user from DB
        user = CustomUser.objects.filter(email=email).first()
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



class LogoutView(APIView):
    def post(self, request):
        if request.user.is_authenticated and request.auth:
            request.auth.delete()
            return Response({
            "message":"You have been logged out successfully!"
            },status=status.HTTP_200_OK)
        else:
            return Response({
                "error":"Token verificartion failed"
            })
            

print('debug', Token)





