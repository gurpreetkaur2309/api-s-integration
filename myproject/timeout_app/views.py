from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from timeout_app.models import CustomUser
from timeout_app.serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class AdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'Admin':
            return Response({"message": "Welcome Admin"})
        return Response({"error": "You are not authorized to view this page"}, status=status.HTTP_403_FORBIDDEN)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'User':
            return Response({"message": "Welcome User"})
        return Response({"error": "You are not authorized to view this page"}, status=status.HTTP_403_FORBIDDEN)
