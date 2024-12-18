from django.utils.timezone import now
from django.contrib.auth import logout

class TimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_active = request.user.last_active
            if (now() - last_active).total_seconds() > 1200:  # 20 minutes
                logout(request)
        response = self.get_response(request)
        if request.user.is_authenticated:
            request.user.last_active = now()
            request.user.save()
        return response
