from django.shortcuts import render
from rest_framework import viewsets
from .models import AuthUser
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer