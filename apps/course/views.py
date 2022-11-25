from django.shortcuts import render

from .models import Course, Group, StudentGroup, QueryCourse
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

from .serializers import CourseSerializer, GroupSerializer, StudentGroupSerializer, QueryCourseSerializer
from rest_framework.permissions import IsAuthenticated

class CourseView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class GroupView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentGroupView(ListCreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer


class QueryCourseView(ListCreateAPIView):
    queryset = QueryCourse.objects.all()
    serializer_class = QueryCourseSerializer


