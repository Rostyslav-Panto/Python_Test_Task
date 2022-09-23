from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post, Feedback


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'description']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['author', 'post_id', 'positive']
        read_only_fields = ['date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                     username=validated_data['username']
                                     )
        user.set_password(validated_data['password'])
        user.save()
        return user
