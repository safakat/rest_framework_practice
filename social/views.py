from django.shortcuts import render
from django.contrib.auth.models import User
from social.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
