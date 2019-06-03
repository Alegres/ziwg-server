from rest_framework import serializers
from apiapp.models import PlantationPreset, User


class PresetSerializer(serializers.Serializer):
    id_user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=30)
    water_per_day = serializers.IntegerField(required=True)
    how_many_times_to_water = serializers.IntegerField(required=True)
    expected_growth = serializers.IntegerField(required=True)
    data_ins = serializers.DateField(required=True)
    min_temp = serializers.FloatField(required=True)
    max_temp = serializers.FloatField(required=True)
    min_soil = serializers.FloatField(required=True)
    max_soil = serializers.FloatField(required=True)
    min_humidity = serializers.FloatField(required=True)
    max_humidity = serializers.FloatField(required=True)

    def create(self, data):
        """
        Create and return a new `PlantationPreset` instance, given the validated data.
        """
        instance = PlantationPreset.objects.create(
            id_user=data.get('id_user'),
            name=data.get('name'),
            how_many_times_to_water=data.get('how_many_times_to_water'),
            water_per_day=data.get('water_per_day'),
            data_ins=data.get('data_ins'),
            min_temp=data.get('min_temp'),
            max_temp=data.get('max_temp'),
            min_soil=data.get('min_soil'),
            max_soil=data.get('max_soil'),
            min_humidity=data.get('min_humidity'),
            max_humidity=data.get('max_humidity'),

        )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationPreset` instance, given the validated data.
        """
        instance.id_user = data.get('id_user', instance.id_user)
        instance.name = data.get('name', instance.name)
        instance.water_per_day = data.get(
            'water_per_day', instance.water_per_day)
        instance.how_many_times_to_water = data.get(
            'how_many_times_to_water', instance.how_many_times_to_water)
        instance.expected_growth = data.get(
            'expected_growth', instance.expected_growth)
        instance.min_temp = data.get('min_temp', instance.min_temp)
        instance.max_temp = data.get('max_temp', instance.max_temp)
        instance.min_soil = data.get('min_soil', instance.min_soil)
        instance.max_soil = data.get('max_soil', instance.max_soil)
        instance.min_humidity = data.get('min_humidity', instance.min_humidity)
        instance.max_humidity = data.get('max_humidity', instance.max_humidity)
        instance.save()
        return instance
