import email
from email.headerregistry import Group
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . import models

# class CreateUserSerializer(UserCreateSerializer):
#   class Meta(UserCreateSerializer.Meta):
#     model = models.User
#     fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = '__all__'
    REQUIRED_FIELDS = ['email','username','password']

  def create(self, validated_data):
    user = models.User.objects.create(
      email=validated_data['email'],
      username=validated_data['username'],
      password=make_password(validated_data['password']),
    )
    group = models.Group.objects.get(id=1)
    user.groups.add(group)
    user.is_superuser = False
    user.is_staff = False
    return user

class JournalSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Journal
    fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Area
    fields = '__all__'

class HabitSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Habits
    fields = '__all__'

class HabitLogSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.HabitLog
    fields = '__all__'

class MoodLogSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.MoodLogs
    fields = '__all__'
