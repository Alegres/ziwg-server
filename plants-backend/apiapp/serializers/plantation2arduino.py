from rest_framework import serializers
from apiapp.models import Plantation2Aduino
from apiapp.models import Plantation

class Plantation2ArduinoSerializer(serializers.Serializer):
    id_plantation = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Plantation.objects.all())
    id = serializers.IntegerField(read_only=True)
    id_arduino = serializers.IntegerField(required=True)

    def create(self, data):
        """
        Create and return a new `PlantationAvg` instance, given the validated data.
        """
        instance = Plantation2Aduino.objects.create(
            id_arduino=data.get('id_arduino'),
            id_plantation=data.get('id_plantation'),
            id=data.get('id'),
                )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationAvg` instance, given the validated data.
        """
        instance.id_plantation = data.get('id_plantation', instance.id_plantation)
        instance.id_arduino = data.get(
            'id_arduino', instance.id_arduino)

        instance.save()
        return instance





