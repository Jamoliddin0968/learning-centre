from django.db import models

from apps.user.models import User
from django.contrib.auth.models import UserManager


class StudentManager(UserManager):
	def get_queryset(self):
		return super().get_queryset().filter(role = "TEACHER")


class Student(User):
	objects = StudentManager()
	class Meta:
		proxy = True
