from rest_framework import serializers
from .models import Profile, Follow
from django.contrib.auth import get_user_model

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



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
