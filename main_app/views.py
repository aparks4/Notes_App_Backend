from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

from .models import User, Note, Profile
from .serializers import UserSerializer, ProfileSerializer, RegisterSerializer, NoteSerializer

from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


# Create your views here.

class Users(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class Users(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request):
#         data = User.objects.all()
#         serializer = UserSerializer(data, many=True)
#         return JsonResponse(serializer.data, safe=False)

# class UserInfo(APIView):
#     def get_user_auth(self, id):
#         return User.objects.all().filter(id=id)
    
#     def get_user_profile(self, id):
#         return Profile.objects.all().filter(user_id=id)

#     def get(self, request, id):
#         user = UserSerializer(self.get_user_auth(id), many=True)
#         profile = ProfileSerializer(self.get_user_profile(id), many=True)
#         return JsonResponse({"user": user.data, "profile": profile.data}, safe=False)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_class = ([])
    serializer_class = RegisterSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user.id)

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
        
