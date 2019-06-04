from rest_framework import serializers
from apiapp.models import Plantation
from apiapp.models import PlantationPreset
from binascii import hexlify
import os
class PlantationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_preset=serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=PlantationPreset.objects.all())
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=30)
    color = serializers.CharField( required=True, max_length=32)
    secret_code = serializers.CharField(required=True, max_length=32)
    def create(self, data):
        """
        Create and return a new `Plantation` instance, given the validated data.
        """
        instance = Plantation.objects.create(
            name=data.get('name'),
            color=data.get('color'),
            id_preset=data.get('id_preset'),
            secret_code=hexlify(os.urandom(32))
        )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `Plantation` instance, given the validated data.
        """
        instance.name = data.get('name', instance.name)
        instance.color = data.get('color', instance.color)
        instance.id_preset = data.get('id_preset', instance.id_preset)
        instance.save()
        return instance

