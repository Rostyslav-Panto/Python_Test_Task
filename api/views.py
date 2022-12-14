from itertools import groupby

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from collections import Counter

from api.models import Post, Feedback, MyUser
from api.serializers import PostSerializer, FeedbackSerializer, UserSerializer


class PostsView(viewsets.ViewSet):
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.filter(author=self.request.user.id)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        post_data = {
            **request.data.dict(),
            "author": f"{self.request.user.id}"
        }
        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(viewsets.ViewSet):
    serializer_class = FeedbackSerializer

    def list(self, request):
        queryset = Feedback.objects.all()
        serializer = FeedbackSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        feedback_data = {
            **request.data.dict(),
            "author": f"{self.request.user.id}"
        }

        serializer = FeedbackSerializer(data=feedback_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_like_analytics(request):
    params = request.query_params
    queryset = Feedback.objects.filter(date__range=[params.get('date_from'), params.get('date_to')])
    print(params.get('date_from'),params.get('date_to'))
    if (not all(param in params for param in ("date_from", "date_to"))
            or params['date_from'] > params['date_to']):
        return Response("Parameters are not valid", status=status.HTTP_400_BAD_REQUEST)
    ordered_queryset = queryset.order_by('date')
    likes_by_date = groupby(ordered_queryset,
                            lambda like: like.date.strftime("%Y-%m-%d"))

    analytics = []
    for date, likes in likes_by_date:
        count = Counter(like.positive for like in likes)
        analytics.append(
            {
                'date': date,
                'total_likes': count.get(True),
                'total_dislikes': count.get(False),

            }
        )
    return Response(analytics, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_activity(request):
    statistics = {
        "User Last Login": request.user.last_login,
        "User Last Activity": MyUser.objects.get(user=request.user).last_activity
    }
    return Response(statistics, status=status.HTTP_200_OK)


class RegisterView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
