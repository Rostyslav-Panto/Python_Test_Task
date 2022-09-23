from rest_framework.routers import DefaultRouter
from api.views import PostView, FeedbackView, RegisterView, AnalyticsView

app_name = 'api'

router = DefaultRouter()
router.register('feedback', FeedbackView, basename='feedback')
# router.register('analytics', AnalyticsView, basename='analytics')
urlpatterns = router.urls
