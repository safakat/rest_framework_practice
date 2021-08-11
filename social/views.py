from django.shortcuts import render
from django.contrib.auth.models import User
from social.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from social.serializers import ProfileSerializer
from social.models import Profile
# Create your views here.

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileAPIView(APIView):

    def get(self, request, format = None):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data,many=True)
        if serializer.is_valid:
            return serializer.data
        else:
            return serializer.default_error_messages