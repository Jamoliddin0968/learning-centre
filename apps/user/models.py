from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib
import uuid


def user_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    name = str(hashlib.sha1(str(instance.id).encode()).hexdigest())
    print(name)
    filename = "%s.%s" % (name, ext)
    return f"user/{filename}"


class User(AbstractUser):
    ROLES = (
        ("TEACHER", "Teacher"),
        ("STUDENT", "Student"),
        ("USER", "user")
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLES, default="USER")
    photo = models.ImageField(upload_to=user_image_rename, default=None)


class TeacherManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="TEACHER")


class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True


class StudentManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="STUDENT")


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True
