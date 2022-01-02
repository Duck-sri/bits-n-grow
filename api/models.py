from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField, create_many_to_many_intermediary_model

from app.settings import DATABASES

from .enums import *
# Create your models here.


class UserProfile(models.Model):
  user   = models.OneToOneField(User,on_delete=models.CASCADE)
  dob = models.DateField()
  avatar = models.ImageField()

  class Meta:
    db_table = 'user_profiles'

class Journal(models.Model):
  name = models.CharField(max_length=100,null=False)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  descrpiption = models.TextField(max_length=500)
  created = models.DateTimeField(null=False)


  def __str__(self):
    return f"{self.name}\n\t{self.descrpiption}"

  class Meta:
    db_table = 'journals'
    ordering = ['name','created']


class Area(models.Model):
  name = models.CharField(max_length=30,null=False)
  created = models.DateField(null=False)

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'areas'
    ordering = ['name','created']
  
  
class Habits(models.Model):
  name = models.CharField(max_length=100,null=False)
  description = models.TextField()
  journal = models.ForeignKey(Journal,on_delete=models.CASCADE)
  notion = models.CharField(
    max_length=10,
    choices=[(tag.value,tag.value) for tag in NOTIONS],
    default=NOTIONS.GOOD.value
  )
  category = models.ForeignKey(Area,on_delete=models.CASCADE)
  time_preffered = models.CharField(
    max_length=20,
    choices=[(tag.value,tag.value) for tag in TIME_OF_DAY],
    default= TIME_OF_DAY.ALL.value
  )
  count_a_day = models.IntegerField(default=1,null=False)

  created = models.DateTimeField(null=False)
  completed = models.IntegerField(default=0,null=False)
  skipped = models.IntegerField(default=0,null=False)
  failed = models.IntegerField(default=0,null=False)
  streak = models.IntegerField(default=0,null=False)

  def total_days(self):
    return self.completed + self.failed + self.skipped

  def __str__(self):
    return f"{self.name}\n\t{self.description}"

  class Meta:
    db_table = 'habits'
    ordering = ['name','created']
  

class MoodLogs(models.Model):
  journal = models.ForeignKey(Journal,on_delete=models.CASCADE)
  mood = models.CharField(
    max_length=10,
    choices=[(tag.value,tag.value) for tag in MOODS],
    default=MOODS.NONE.value,
    null=False
  )
  created = models.DateTimeField(null=False)
  note = models.TextField(null=False,default="")    

  def __str__(self): return self.mood

  class Meta:
    db_table = 'mood_logs'
    ordering = ['created']


class HabitLog(models.Model):
  habit = models.ForeignKey(Habits,on_delete=models.CASCADE)
  time = models.DateTimeField(null=False)
  status = models.CharField(
    max_length=10,
    choices=[(tag.value,tag.value) for tag in LOG_STATUS]
  )
  notes = models.TextField(default="")

  class Meta:
    db_table = 'habit_logs'