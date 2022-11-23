from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    ROLE = "USER"

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',"username",
                  'phone', 'password','password',"photo")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.role = self.ROLE
        user.set_password(validated_data['password'])
        user.save()
        return user

class TeacherSerializer(UserSerializer):
    ROLE = "TEACHER"

class StudentSerializer(UserSerializer):
    ROLE = "STUDENT"

class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","phone","photo")