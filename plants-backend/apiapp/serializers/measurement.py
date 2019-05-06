from rest_framework import serializers
from apiapp.models import PlantationAvg
from apiapp.models import Plantation

class PlantationAvgSerializer(serializers.Serializer):
    id_plantation = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Plantation.objects.all())
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=30)
    good_temperature = serializers.IntegerField(required=True)
    good_humidity = serializers.IntegerField(required=True)
    water_per_day = serializers.IntegerField(required=True)
    how_many_times_to_water = serializers.IntegerField(required=True)
    expected_growth = serializers.IntegerField(required=True)

    def create(self, data):
        """
        Create and return a new `PlantationAvg` instance, given the validated data.
        """
        instance = PlantationAvg.objects.create(
            name=data.get('name'),
            good_temperature=data.get('good_temperature'),
            good_humidity=data.get('good_humidity'),
            water_per_day=data.get('water_per_day'),
            how_many_times_to_water=data.get('how_many_times_to_water'),
            expected_growth=data.get('expected_growth'),
                )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationAvg` instance, given the validated data.
        """
        instance.name = data.get('name', instance.name)
        instance.good_temperature = data.get(
            'good_temperature', instance.good_temperature)
        instance.good_humidity = data.get(
            'good_humidity', instance.good_humidity)
        instance.water_per_day = data.get(
            'water_per_day', instance.water_per_day)
        instance.how_many_times_to_water = data.get(
            'how_many_times_to_water', instance.how_many_times_to_water)
        instance.expected_growth = data.get(
            'expected_growth', instance.expected_growth)

        instance.save()
        return instance
