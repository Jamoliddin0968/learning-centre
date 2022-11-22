from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

import uuid

def user_image_rename(instance, filename):
    ext = filename.split('.')[-1]
    name = str(instance.id)
    filename = "%s.%s" % (name, ext)
    return f"user/{filename}"

class User(AbstractUser):
	ROLES = (
			("ADMIN","Admin"),
			("TEACHER","Teacher"),
			("STUDENT","Student"),
			("GUEST","guest")
		)
	id = models.UUIDField(default=uuid.uuid4,unique = True,primary_key = True)
	role = models.CharField(max_length = 10,choices = ROLES,default = "GUEST")
	photo = models.ImageField(upload_to=user_image_rename)





