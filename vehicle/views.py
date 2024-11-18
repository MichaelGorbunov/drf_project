from django.shortcuts import render
from rest_framework import viewsets
from vehicle.serializers import CarSerializer
from vehicle.models import Car



# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()