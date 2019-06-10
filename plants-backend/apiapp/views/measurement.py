from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import PlantationMeasurements
from apiapp.models import PlantationPreset
from apiapp.models import Plantation, PlantationAvg, Plantation2Arduino
from apiapp.serializers.measurement import PlantationMeasurementsSerializer
from apiapp.utils.jsonreader import JsonReader
from apiapp.security.voters import UserVoter
from apiapp.views.sendInfo import inform_user
import datetime
@api_view(['GET', 'PUT'])
def api_measurement(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    plant_inst = PlantationMeasurements.objects.filter(id_plantation=pk)
    if not plant_inst:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantationMeasurementsSerializer(plant_inst, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        voter = UserVoter(request)
        data = JsonReader.read_body(request)
        if not voter.is_superuser():
            return Response({'error': "Non admin cannot update admin attributes"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PlantationMeasurementsSerializer(plant_inst, data=data)
        if serializer.is_valid():
            serializer.save()
            if not checkIfMeasurementsAreOk(serializer.data):
                inform_user(serializer.data['id_plantation'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_admin_measurement_index(request):
    """
    get:
    List all plants.
    post:
    Create new plants.
    """
   # voter = UserVoter(request)
  # if not voter.is_superuser():
  #      return Response({'error': "Plant API is not allowed by non admin user"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = PlantationMeasurementsSerializer(
            PlantationMeasurements.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonReader.read_body(request)
        try:
            plantation2arduino = Plantation2Arduino.objects.get(
                id_arduino=data['id_arduino'])
        except Plantation2Arduino.DoesNotExist:
            return Response("Arduino not found", status=status.HTTP_404_NOT_FOUND)

        data_copy = data.copy()
        data_copy['id_plantation'] = plantation2arduino.id_plantation.id
        serializer = PlantationMeasurementsSerializer(data=data_copy)
        if serializer.is_valid():
            print("is_valid = 1")
            serializer.save()
            changeAvg(serializer.data['id_plantation'])
            if not checkIfMeasurementsAreOk(serializer.data):
                inform_user(serializer.data['id_plantation'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def checkIfMeasurementsAreOk(measurementtData):
    id = measurementtData.get('id_plantation')
    plantation = Plantation.objects.get(pk=id)
    preset = PlantationPreset.objects.get(pk=plantation.id_preset.id)
    return isBetweenValues(preset.min_soil, preset.max_soil, measurementtData['soil']) and isBetweenValues(preset.min_temp, preset.max_temp, measurementtData['temp']) and isBetweenValues(preset.min_humidity, preset.max_humidity, measurementtData['humidity'])


def isBetweenValues(min, max, value):
    return min <= value <= max


def changeAvg(idPlantation):
    sumTmp = 0
    sumSoil = 0
    sumHumidity = 0
    avg = PlantationAvg.objects.get(id_plantation=idPlantation)
    measurements = PlantationMeasurements.objects.filter(
        id_plantation=idPlantation).order_by('-data_ins')[:10]
    for measurement in measurements:
        sumTmp += measurement.temp
        sumSoil += measurement.soil
        sumHumidity += measurement.humidity
    sumHumidity = sumHumidity/(measurements.count())
    sumTmp = sumTmp/(measurements.count())
    sumSoil = sumSoil/(measurements.count())
    print(sumHumidity)
    print(sumSoil)
    print(sumTmp)
    print(measurements.count())

    print(not avg)
    if not avg:
        newAvg = PlantationAvg(id_plantation=idPlantation,
                               temp=sumTmp, soil=sumSoil, humidity=sumHumidity)
        newAvg.save()
    else:
        avg.temp = sumTmp
        avg.soil = sumSoil
        avg.humidity = sumHumidity
        avg.save()
