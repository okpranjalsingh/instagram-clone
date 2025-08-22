from rest_framework import serializers
from .models import (
    CustomUser,
)

'''
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'bio', 'profile_picture']
'''

class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = 'CustomUser'
        fields = ['id', 'username', 'email', 'password']


    def create(self, validated_data):
        user = CustomUser(
            username = self.validated_data['username'],
             email = self.validated_data['email']

        )

        user.set_password(validated_data['pass'])
        


