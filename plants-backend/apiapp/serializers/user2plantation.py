from rest_framework import serializers
from apiapp.models import Plantation, User, User2Plantation


class User2PlantationSerializer(serializers.Serializer):
    id_plantation = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Plantation.objects.all())
    id = serializers.IntegerField(read_only=True)
    id_user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())

    def create(self, data):
        """
        Create and return a new `PlantationAvg` instance, given the validated data.
        """
        instance = User2Plantation.objects.create(
            id_plantation=data.get('id_plantation'),
            id_user=data.get('id_user'),
        )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationAvg` instance, given the validated data.
        """
        instance.id_user = data.get('id_user', instance.id_user)
        instance.id_plantation = data.get(
            'id_plantation', instance.id_plantation)

        instance.save()
        return instance
