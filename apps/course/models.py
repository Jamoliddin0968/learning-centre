from django.db import models
import uuid
from datetime import datetime

def course_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    name = str(datetime.now()).replace("-", "").replace(".","")
    filename = "%s.%s" % (name, ext)
    return f"course/{filename}"


class Course(models.Model):
	id = models.UUIDField(default=uuid.uuid4,primary_key = True,unique = True)
	name = models.CharField(max_length = 70)
	logo = models.ImageField(upload_to=course_image_rename,default = None)
	teacher = models.ForeignKey('user.Teacher',on_delete = models.CASCADE)
	description = models.TextField()
	period = models.CharField(max_length = 15)

class Group(models.Model):
	name = models.CharField(max_length = 10)
	course = models.ForeignKey('course.Course',on_delete = models.CASCADE)
	start_time = models.DateTimeField(auto_now_add = True)
	end_time = models.DateTimeField(auto_now_add = True)
	is_active = models.BooleanField(default = False)