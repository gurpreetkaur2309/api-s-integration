from django.urls import path
from timeout_app.views import RegisterView, LoginView, AdminView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', AdminView.as_view(), name='admin'),
    path('user/', UserView.as_view(), name='user'),
]
