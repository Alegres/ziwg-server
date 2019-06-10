from rest_framework import serializers
from apiapp.models import PlantationMeasurements
from apiapp.models import Plantation
from datetime import date


class PlantationMeasurementsSerializer(serializers.Serializer):
    id_plantation = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Plantation.objects.all())
    id = serializers.IntegerField(read_only=True)
    temp = serializers.FloatField(required=True)
    soil = serializers.FloatField(required=True)
    humidity = serializers.FloatField(required=True)
    data_ins = serializers.TimeField(required=False)

    def create(self, data):
        """
        Create and return a new `PlantationAvg` instance, given the validated data.
        """
        instance = PlantationMeasurements.objects.create(
         #   data_ins=date.today(),
            id_plantation=data.get('id_plantation'),
            soil=data.get('soil'),
            data_ins=date.fromtimestamp(),
            temp=data.get('temp'),
            humidity=data.get('humidity'),
        )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationAvg` instance, given the validated data.
        """
        instance.data_ins = data.get('data_ins', instance.data_ins)
        instance.id_plantation = data.get(
            'id_plantation', instance.id_plantation)
        instance.soil = data.get(
            'soil', instance.soil)
        instance.temp = data.get(
            'temp', instance.temp)
        instance.humidity = data.get(
            'humidity', instance.humidity)

        instance.save()
        return instance
