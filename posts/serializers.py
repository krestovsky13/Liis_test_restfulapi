from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="email", queryset=get_user_model().objects.all())

    class Meta:
        model = Post
        fields = ("id", "title", "created_at", "author")


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="email", queryset=get_user_model().objects.all())

    class Meta:
        model = Post
        fields = '__all__'


class ChangePostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="email", queryset=get_user_model().objects.all())

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author')
