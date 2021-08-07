from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from accounts.models import Profile
from accounts.serializers import ProfileSerializer

# Create your views here.

class CreateProfile(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ListProfile(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
