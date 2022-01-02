from django.urls import path

from . import views

urlpatterns = [
  path('',views.getHi,name="Hello world")
]