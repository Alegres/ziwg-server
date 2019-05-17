from rest_framework import serializers
from apiapp.models import PlantationAvg
from apiapp.models import Plantation

class PlantationAvgSerializer(serializers.Serializer):
    id_plantation = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Plantation.objects.all())
    id = serializers.IntegerField(read_only=True)
    temp = serializers.FloatField(required=True)
    soil = serializers.FloatField(required=True)
    humidity = serializers.FloatField(required=True)

    def create(self, data):
        """
        Create and return a new `PlantationAvg` instance, given the validated data.
        """
        instance = PlantationAvg.objects.create(
            soil=data.get('soil'),
            id_plantation=data.get('id_plantation'),
            temp=data.get('temp'),
            humidity=data.get('humidity'),
                )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationAvg` instance, given the validated data.
        """
        instance.soil = data.get(
            'soil', instance.soil)
        instance.id_plantation = data.get('id_plantation', instance.id_plantation)
        instance.temp = data.get(
            'temp', instance.temp)
        instance.humidity = data.get(
            'humidity', instance.humidity)

        instance.save()
        return instance

