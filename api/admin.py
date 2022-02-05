from django.contrib import admin

from . import models
# Register your models here.

admin.site.register([
  # models.User, # already registerd by admin
  models.Journal,
  models.Area,
  models.Habits,
  models.HabitLog,
  models.MoodLogs,
])