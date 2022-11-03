from contextvars import Token
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
		"Endpoint": "/user/token",
		"method": "POST",
		"body": {
			"Username": "",
			"Password": ""
		},
		"description": "Returns token"
		},
        {
		"Endpoint": "/user/token/refresh",
		"method": "POST",
		"body": {"Refresh": ""},
		"description": "Returns refreshed token"
		},
        {
		"Endpoint": "/user/register",
		"method": "POST",
		"body": {
            "username": "",
            "password": "",
            "password2": ""
        },
		"description": "Returns token"
		},
		{
		"Endpoint": "/user/login",
		"method": "POST",
		"body": {
            "username": "",
            "password": "",
            "password2": ""
        },
		"description": "Returns token"
		},
    ]
    return Response(routes)