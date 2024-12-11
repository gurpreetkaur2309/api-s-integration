from django.shortcuts import render

# # Create your views here.
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

saml_config = settings.SAML_CONFIG
# # Custom welcome view
# @api_view(['GET'])
# def welcome_view(request):
#     return Response({"message": "Welcome to JWT implementation in Django!"})

# # Protected user view
# @api_view(['GET'])
# def user_view(request):
#     user = request.user
#     serializer = UserSerializer(user)
#     return Response(serializer.data)
class Home(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		content = {'message' : 'Hello World'}
		return Response(content)
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

# Serializer for Register
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

# Serializer for Login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                })
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# auth_app/views.py (Add this to your existing views)
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view, you are authenticated!"})
class SamlLoginView(APIView):
     def get(self,request):
          return Response({"messege":"Redirect to SAML identity provider for authentication"})
class SamlACSView(APIView):
     def post(self,request):
          user_data={
               'username':request.data.get('username'),
               'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name')
          }
          user, created = User.objects.get_or_create(username=user_data['username'])
               
          user.first_name = user_data['first_name']
          user.last_name = user_data['last_name']
          user.save()  
          #Generate teh jwt token for this
          refresh = RefreshToken.for_user(user)
          access_token = str(refresh.access_token)  
          return Response({
                  'access' : access_token,
                  'refresh' : str(refresh)
              })
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, Address, Product, Cart, Order, Payment, OrderPlaced
from .serializers import (
    ContactSerializer,
    AddressSerializer,
    ProductSerializer,
    CartSerializer,
    OrderSerializer,
    PaymentSerializer,
    OrderPlacedSerializer,
)

# Generic API for CRUD Operations
class GenericAPIView(APIView):
    model = None
    serializer_class = None
    
    def get(self, request, pk=None):
        print("mode",self.model)
        if pk:
            
            instance = self.model.objects.filter(pk=pk).first()
            if not instance:
                return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(instance)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        instance = self.model.objects.filter(pk=pk).first()
        if not instance:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        instance = self.model.objects.filter(pk=pk).first()
        if not instance:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# API Endpoints
class ContactAPIView(GenericAPIView):
    model = Contact
    serializer_class = ContactSerializer

class AddressAPIView(GenericAPIView):
    model = Address
    serializer_class = AddressSerializer

class ProductAPIView(GenericAPIView):
    model = Product
    serializer_class = ProductSerializer

class CartAPIView(GenericAPIView):
    model = Cart
    serializer_class = CartSerializer

class OrderAPIView(GenericAPIView):
    model = Order
    serializer_class = OrderSerializer

class PaymentAPIView(GenericAPIView):
    model = Payment
    serializer_class = PaymentSerializer

class OrderPlacedAPIView(GenericAPIView):
    model = OrderPlaced
    serializer_class = OrderPlacedSerializer
