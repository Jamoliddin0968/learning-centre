from rest_framework import serializers
from .models import Course , Group , StudentGroup , QueryCourse

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = "__all__"
class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"
class StudentGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentGroup
		fields = "__all__"
class QueryCourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = QueryCourse
		fields = "__all__"
