from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views

from .views import OTHER,JournalViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('journals',JournalViewSet)
router.register('users',UserViewSet)

urlpatterns = router.urls + OTHER + [

]