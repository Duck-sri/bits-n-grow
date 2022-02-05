from django.urls import path

from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

from . import serializers as S # serializers
from . import models as M # models

OTHER = []

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = M.User.objects.all()
  serializer_class = S.UserSerializer

class JournalViewSet(viewsets.ModelViewSet):
  queryset = M.Journal.objects.all()
  serializer_class = S.JournalSerializer
  permission_classes = [IsAuthenticated]