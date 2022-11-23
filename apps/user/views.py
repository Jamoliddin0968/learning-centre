from django.shortcuts import render

from rest_framework.generics import CreateAPIView , RetrieveUpdateDestroyAPIView as dtView
from .models import User


from .serializers import UserSerializer , TeacherSerializer,StudentSerializer ,ChangeSerializer


class UserRegister(CreateAPIView):
	queryset = User.objects.all()
	serializer_class =  UserSerializer

class TeacherRegister(CreateAPIView):
	queryset = User.objects.all()
	serializer_class =  TeacherSerializer

class StudentRegister(CreateAPIView):
	queryset = User.objects.all()
	serializer_class =  StudentSerializer

class UserChange(dtView):
	queryset = User.objects.all()
	serializer_class = ChangeSerializer
