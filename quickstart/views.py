from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serialisers import UserSerializer, GroupSerializer
from rest_framework import viewsets, permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]


# Create your views here.
