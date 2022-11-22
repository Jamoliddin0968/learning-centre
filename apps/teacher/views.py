from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView

class index(ListView):
	model = Teacher
	template_name = "in.html"