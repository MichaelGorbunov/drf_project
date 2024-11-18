from rest_framework import serializers
from vehicle.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Car
        fielsd ="__all__"