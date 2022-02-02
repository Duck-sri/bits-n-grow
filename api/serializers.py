from rest_framework import serializers
from . import models

class HabiterSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Habiter
    fields = '__all__'

class JournalSerialier(serializers.Serializer):
  class Meta:
    model = models.Journal
    fields = '__all__'

class AreaSerialier(serializers.Serializer):
  class Meta:
    model = models.Area
    fields = '__all__'

class HabitSerialier(serializers.Serializer):
  class Meta:
    model = models.Habits
    fields = '__all__'

class HabitLogSerialier(serializers.Serializer):
  class Meta:
    model = models.HabitLog
    fields = '__all__'

class MoodLogSerialier(serializers.Serializer):
  class Meta:
    model = models.MoodLogs
    fields = '__all__'
