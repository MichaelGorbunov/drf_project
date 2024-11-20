from rest_framework import serializers
from vehicle.models import Car, Moto, Milage


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Milage
        fields ="__all__"

class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source="milage_set.all.first.milage")
    milage= MilageSerializer(source="milage_set",many=True)

    class Meta:
        model= Car
        fields ="__all__"

class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()
    class Meta:
        model= Moto
        fields ="__all__"
    def get_last_milage(self,instance):
        # if instance.milage_set.all().first():
        #     return instance.milage_set.all().first().milage
        # return 0
        milage = instance.milage_set.first()#сразу первое значение
        if not milage:
            return 0
        return milage.milage

class MotoMilageSerializer(serializers.ModelSerializer):
    # moto = MotoSerializer()
    model = Milage
    # fields=("milage","year","moto",)
    fields = ("milage", "year", )