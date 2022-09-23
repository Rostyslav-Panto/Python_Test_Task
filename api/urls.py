from rest_framework.routers import DefaultRouter
from api.views import PostView, FeedbackView, AnalyticsView

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostView, basename='posts')
router.register('feedback', FeedbackView, basename='feedback')
router.register('analytics', AnalyticsView, basename="analytics")
urlpatterns = router.urls
