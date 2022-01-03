from decimal import InvalidContext
from django.urls import path

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserProfileSerializer

from .models import UserProfile


OTHER = []
GET = []
PUT = []
POST = []
DELETE = []

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List' : '/task-list/',
    'Detailed View' : '/task-list/<str:pk>',
    'Create' : '/task-create/',
    'Update' : '/task-update/<str:pk>',
    'Delete' : '/task-delete/<str:pk>',
  }

  return Response(api_urls)
OTHER.append(path('',apiOverview,name='API overview'))

@api_view(['GET'])
def getUsers(request):
  users =  UserProfile.objects.all()
  serializer = UserProfileSerializer(users,many=True)
  return Response(serializer.data)
GET.append(path('users/',getUsers,name="List Users"))

@api_view(['GET'])
def getUserDetail(request,pk):
  users =  UserProfile.objects.get(id=pk)
  serializer = UserProfileSerializer(users,many=False)
  return Response(serializer.data)
GET.append(path('users/<str:pk>/',getUserDetail,name="Detail single user"))

@api_view(['POST'])
def createUser(request):
  serializer = UserProfileSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  else:
    print("Got Invalid User...")

  return Response(serializer.data)
POST.append(path('user-add/',createUser))