from django.shortcuts import render
from .models import Payment
from rest_framework.generics import CreateAPIView
from .serializers import PaymentSerializer

class PaymentCreate(CreateAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer