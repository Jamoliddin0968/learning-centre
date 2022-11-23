from django.contrib import admin
from .models import Course,Group

admin.site.register((Course,Group))
