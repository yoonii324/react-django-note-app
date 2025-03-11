from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # so that we don't create the user that already exists
    serializer_class = User # tells this view what kind of data we need to accept to make a new user
    permission_classes = [AllowAny] # who can actually call this