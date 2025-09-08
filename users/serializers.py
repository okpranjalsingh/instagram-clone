from rest_framework import serializers
from users.models import CustomUser
from users.models import Follow

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )

        # password hashing
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.ReadOnlyField(source='follower.username')
    following_username = serializers.ReadOnlyField(source='following.username')

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'follower_username', 'following', 'following_username', 'created_at']
        read_only_fields = ['follower', 'created_at']

