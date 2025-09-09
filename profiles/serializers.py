from rest_framework import serializers
from users.models import Follow
from .models import Profile
from django.contrib.auth import get_user_model

class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    profile_pic = serializers.ImageField(source='profile_pic', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'profile_pic', 'followers_count', 'following_count', 'dob', 'gender']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.user.following.count()

User = get_user_model()
class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'profile_picture', 'followers_count', 'following_count']

    def get_followers_count(self, obj):
        return Follow.objects.filter(following=obj.user).count()

    def get_following_count(self, obj):
        return Follow.objects.filter(follower=obj.user).count()
