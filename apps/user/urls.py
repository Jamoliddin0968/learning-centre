from django.urls import path
from .views import (
    StudentRegister, TeacherRegister, UserRegister,
    UserChange,
)
urlpatterns = [
    path("user/create/", UserRegister.as_view()),
    path("student/create/", StudentRegister.as_view()),
    path("teacher/create/", TeacherRegister.as_view()),
    path("student/<uuid:pk>/change/", UserChange.as_view()),
    path("user/<uuid:pk>/change/", UserChange.as_view()),
    path("teacher/<uuid:pk>/change/", UserChange.as_view()),
]
