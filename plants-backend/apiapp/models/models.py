from django.db import models
from .user import User
from django.db.models.signals import post_save

from django.dispatch import receiver


class Plantation(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    good_temperature = models.IntegerField(blank=True, null=True)
    good_humidity = models.IntegerField(blank=True, null=True)
    water_per_day = models.IntegerField(blank=True, null=True)
    how_many_times_to_water = models.IntegerField(blank=True, null=True)
    expected_growth = models.IntegerField(blank=True, null=True)
    data_ins = models.DateField()


class PlantationAvg(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    good_temperature = models.IntegerField(blank=True, null=True)
    good_humidity = models.IntegerField(blank=True, null=True)
    water_per_day = models.IntegerField(blank=True, null=True)
    how_many_times_to_water = models.IntegerField(blank=True, null=True)
    expected_growth = models.IntegerField(blank=True, null=True)


class PlantationHist(models.Model):

    name = models.CharField(max_length=30)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    good_temperature = models.IntegerField(blank=True, null=True)
    good_humidity = models.IntegerField(blank=True, null=True)
    water_per_day = models.IntegerField(blank=True, null=True)
    how_many_times_to_water = models.IntegerField(blank=True, null=True)
    expected_growth = models.IntegerField(blank=True, null=True)
    data_ins = models.DateField()


class User2Plantation(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Plantation2Aduino(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    id_arduino = models.IntegerField(null=False, blank=False)
    secret_code = models.CharField(max_length=32)


class PlantationPreset(models.Model):

    name = models.CharField(max_length=30)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    good_temperature = models.IntegerField(blank=True, null=True)
    good_humidity = models.IntegerField(blank=True, null=True)
    water_per_day = models.IntegerField(blank=True, null=True)
    how_many_times_to_water = models.IntegerField(blank=True, null=True)
    expected_growth = models.IntegerField(blank=True, null=True)
    data_ins = models.DateField()
