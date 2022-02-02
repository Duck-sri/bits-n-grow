from django.urls import path

from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework import views, viewsets, permissions
from rest_framework.response import Response

from . import serializers as S # serializers
from . import models as M # models

OTHER = []
# TODO
# TODO make everything in a ViewSet
# TODO
# Create your views here.

class HabiterViewSet(viewsets.ModelViewSet):
  queryset = M.Habiter.objects.all()
  # permission_classes = [
  #   permissions.IsAuthenticated,
  # ]
  serializer_class = S.HabiterSerializer

  def create(self, validated_data):
    user = super(HabiterViewSet, self).create(validated_data)
    # TODO passwords are not hashed in api request format
    user.set_password(validated_data['password'])
    user.save()
    return user

class JournalViewSet(viewsets.ModelViewSet):
  queryset = M.Journal.objects.all()
  # permission_classes = [
  #   permissions.IsAuthenticated  
  # ]
  serializer_class = S.JournalSerialier