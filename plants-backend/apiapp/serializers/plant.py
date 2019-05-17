from rest_framework import serializers
from apiapp.models import Plantation
from apiapp.models import PlantationPreset


class PlantationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_preset=serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=PlantationPreset.objects.all())
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=30)

    def create(self, data):
        """
        Create and return a new `Plantation` instance, given the validated data.
        """
        instance = Plantation.objects.create(
            name=data.get('name'),
            id_preset=data.get('id_preset'),
        )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `Plantation` instance, given the validated data.
        """
        instance.name = data.get('name', instance.name)
        instance.id_preset = data.get('id_preset', instance.id_preset)
        instance.save()
        return instance

