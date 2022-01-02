from django.contrib import admin

from . import models
# Register your models here.

admin.site.register([
  models.UserProfile,
  models.Journal,
  models.Area,
  models.Habits,
  models.HabitLog,
  models.MoodLogs,
])