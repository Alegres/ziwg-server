from django.db import models
from .user import User
from django.db.models.signals import post_save

from django.dispatch import receiver


class PlantationPreset(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    water_per_day = models.IntegerField(blank=True, null=True)
    how_often_to_water = models.IntegerField(blank=True, null=True)
    expected_growth = models.IntegerField(blank=True, null=True)
    how_long_to_water= models.IntegerFIeld(blank=True,null=True)
    data_ins = models.DateField()
    min_temp = models.FloatField(blank=True, null=True)
    max_temp = models.FloatField(blank=True, null=True)
    min_soil = models.FloatField(blank=True, null=True)
    max_soil = models.FloatField(blank=True, null=True)
    min_humidity = models.FloatField(blank=True, null=True)
    max_humidity = models.FloatField(blank=True, null=True)
    color= models.CharField(blank=True,null=True, max_length=32)

class Plantation(models.Model):
    id = models.AutoField(primary_key=True)
    id_preset = models.ForeignKey(
        PlantationPreset, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    color = models.CharField(blank=True, null=True, max_length=32)
    secret_code = models.CharField(max_length=32, null=True)


class PlantationMeasurements(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    temp = models.FloatField(blank=True, null=True)
    soil = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    data_ins = models.DateField(null=True)


class PlantationAvg(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    temp = models.FloatField(blank=True, null=True)
    soil = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)


class User2Plantation(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Plantation2Arduino(models.Model):

    id = models.AutoField(primary_key=True)
    id_plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE)
    id_arduino = models.IntegerField(null=False, blank=False)
