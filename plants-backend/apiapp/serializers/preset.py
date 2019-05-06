from rest_framework import serializers
from apiapp.models import PlantationPreset, User


class PresetSerializer(serializers.Serializer):
    id_user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=30)
    good_temperature = serializers.IntegerField(required=True)
    good_humidity = serializers.IntegerField(required=True)
    water_per_day = serializers.IntegerField(required=True)
    how_many_times_to_water = serializers.IntegerField(required=True)
    expected_growth = serializers.IntegerField(required=True)
    data_ins = serializers.DateField(required=True)

    def create(self, data):
        """
        Create and return a new `PlantationPreset` instance, given the validated data.
        """
        instance = PlantationPreset.objects.create(
            id_user=data.get('id_user'),
            name=data.get('name'),
            good_temperature=data.get('good_temperature'),
            good_humidity=data.get('good_humidity'),
            water_per_day=data.get('water_per_day'),
            how_many_times_to_water=data.get('how_many_times_to_water'),
            expected_growth=data.get('expected_growth'),
            data_ins=data.get('data_ins'),
        )
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `PlantationPreset` instance, given the validated data.
        """
        instance.id_user = data.get('id_user', instance.id_user)
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
        instance.data_ins = data.get('data_ins', instance.data_ins)
        instance.save()
        return instance
