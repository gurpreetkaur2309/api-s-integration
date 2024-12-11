from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Home
from .views import RegisterView, LoginView, ProtectedView,SamlACSView,SamlLoginView
from rest_framework_simplejwt import views as jwt_views
from authapp import views
from .views import (
    ContactAPIView,
    AddressAPIView,
    ProductAPIView,
    CartAPIView,
    OrderAPIView,
    PaymentAPIView,
    OrderPlacedAPIView,
)
urlpatterns = [
    path('', Home.as_view(), name='welcome'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('sso/login/', SamlLoginView.as_view(), name='saml_login'),  # SAML login redirect
    path('sso/acs/', SamlACSView.as_view(), name='saml_acs'), 
    path('api/contact/', ContactAPIView.as_view(), name='contact_list'),
    path('api/contact/<int:pk>/', ContactAPIView.as_view(), name='contact_detail'),
    path('api/address/', AddressAPIView.as_view(), name='address_list'),
    path('api/address/<int:pk>/', AddressAPIView.as_view(), name='address_detail'),
    path('api/product/', ProductAPIView.as_view(), name='product_list'),
    path('api/product/<int:pk>/', ProductAPIView.as_view(), name='product_detail'),
    path('api/cart/', CartAPIView.as_view(), name='cart_list'),
    path('api/cart/<int:pk>/', CartAPIView.as_view(), name='cart_detail'),
    path('api/order/', OrderAPIView.as_view(), name='order_list'),
    path('api/order/<int:pk>/', OrderAPIView.as_view(), name='order_detail'),
    path('api/payment/', PaymentAPIView.as_view(), name='payment_list'),
    path('api/payment/<int:pk>/', PaymentAPIView.as_view(), name='payment_detail'),
    path('api/orderplaced/', OrderPlacedAPIView.as_view(), name='orderplaced_list'),
    path('api/orderplaced/<int:pk>/', OrderPlacedAPIView.as_view(), name='orderplaced_detail'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('user/', user_view, name='user'),  # Protected endpoint
]
