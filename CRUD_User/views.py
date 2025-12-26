from django.shortcuts import render
from rest_framework.decorators import api_view
from CRUD_User.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics
from CRUD_User.models import User

# Create your views here
@api_view(['GET', 'POST'])
def UserView(request):
  if request.method == 'GET':
    users = User.objects.all()
    serializedUsers = UserSerializer(users, many=True)
    return Response(serializedUsers)

class userView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class detailedUserView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'pk'

