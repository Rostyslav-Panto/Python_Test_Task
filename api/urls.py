from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import PostsView, FeedbackView, RegisterView, get_user_activity, get_like_analytics

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostsView, basename='posts')
router.register('feedback', FeedbackView, basename='feedback')
router.register('register', RegisterView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', get_like_analytics),
    path('user-info/', get_user_activity)
]
