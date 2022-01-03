from django.urls import path

from .views import GET,POST,PUT,DELETE,OTHER

urlpatterns = [

] + GET + POST + PUT + DELETE + OTHER
