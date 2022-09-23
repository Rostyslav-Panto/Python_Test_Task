from rest_framework.routers import DefaultRouter
from api.views import PostsView, FeedbackView, RegisterView, AnalyticsView

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostsView, basename='posts')
router.register('feedback', FeedbackView, basename='feedback')
router.register('analytics', AnalyticsView, basename='analytics')
router.register('register', RegisterView, basename='register')
urlpatterns = router.urls
