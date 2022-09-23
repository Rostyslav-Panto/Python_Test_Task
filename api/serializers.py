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
