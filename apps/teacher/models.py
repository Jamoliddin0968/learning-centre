from django.db import models

from apps.user.models import User
from django.contrib.auth.models import UserManager


class TeacherManager(UserManager):
	def get_queryset(self):
		return super().get_queryset().filter(role = "TEACHER")


class Teacher(User):
	objects = TeacherManager()
	class Meta:
		proxy = True
