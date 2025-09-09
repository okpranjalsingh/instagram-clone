from rest_framework import serializers
from .models import (
    Post,
    Comment,
    Like
)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'caption', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class CommentsSerializers(serializers.ModelSerializer):
    model = Comment
    fields = ['id', 'user', 'post', 'content', 'created_at', 'updated_at']
    read_only_fields = ['user', 'post', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user', 'post', 'created_at']
        read_only_fields = ['user', 'created_at']





