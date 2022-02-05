from socket import timeout
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,Group,User
from sqlalchemy import true

from .enums import *
# Create your models here.

# User is already used from django

class Journal(models.Model):
  name = models.CharField(max_length=100,null=False)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  descrpiption = models.TextField(max_length=500,blank=True,default="")
  created = models.DateTimeField(default=timezone.now,null=False,db_index=True)


  def __str__(self):
    return f"{self.name}"

  class Meta:
    db_table = 'journals'
    ordering = ['name','created']


class Area(models.Model):
  name = models.CharField(max_length=30,null=False)
  created = models.DateField(default=timezone.now,null=False)

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'areas'
    ordering = ['name','created']
  
  
class Habits(models.Model):
  name = models.CharField(max_length=100,null=False)
  description = models.TextField(blank=True,default="")
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

  created = models.DateTimeField(default=timezone.now,null=False,db_index=True)
  completed = models.IntegerField(default=0,null=False)
  skipped = models.IntegerField(default=0,null=False)
  failed = models.IntegerField(default=0,null=False)
  streak = models.IntegerField(default=0,null=False)

  def total_days(self):
    return self.completed + self.failed + self.skipped

  def __str__(self):
    return f"{self.name}"

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
  created = models.DateTimeField(default=timezone.now,null=False,db_index=True)
  note = models.TextField(blank=False,default="")    

  def __str__(self): return f"{self.mood} {self.created}"

  class Meta:
    db_table = 'mood_logs'
    ordering = ['created']


class HabitLog(models.Model):
  habit = models.ForeignKey(Habits,on_delete=models.CASCADE)
  time = models.DateTimeField(default=timezone.now,null=False,db_index=True)
  status = models.CharField(
    max_length=10,
    choices=[(tag.value,tag.value) for tag in LOG_STATUS]
  )
  notes = models.TextField(default="",blank=True,null=True)

  def __str__(self):
    habit_name = self.habit.name
    time = self.time
    return f"{habit_name} : {time}"

  class Meta:
    db_table = 'habit_logs'