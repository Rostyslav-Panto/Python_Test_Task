from django.utils import timezone

from api.models import MyUser


class LastActivityTraceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            MyUser.objects.filter(user=request.user) \
                .update(last_activity=timezone.now())
        return response