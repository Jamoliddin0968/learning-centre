from django.urls import path
from .views import StudentRegister, TeacherRegister, UserRegister
urlpatterns = [
    path("user_create/",UserRegister.as_view()),
    path("student_create/",StudentRegister.as_view()),
    path("teacher_create/",TeacherRegister.as_view()),
]
