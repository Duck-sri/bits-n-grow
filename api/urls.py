from django.urls import path
from rest_framework import routers

from .views import OTHER,JournalViewSet,HabiterViewSet

router = routers.DefaultRouter()
router.register('journals',JournalViewSet)
router.register('users',HabiterViewSet)

urlpatterns = router.urls + OTHER + [

]