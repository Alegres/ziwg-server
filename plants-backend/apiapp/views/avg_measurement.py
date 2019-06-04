from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import PlantationAvg
from apiapp.serializers.avg_measurement import PlantationAvgSerializer
from apiapp.utils.jsonreader import JsonReader
from apiapp.security.voters import UserVoter


@api_view(['GET', 'PUT'])
def api_avg_measurement(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    try:
        plant_inst = PlantationAvg.objects.get(id_plantation=pk)
    except PlantationAvg.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantationAvgSerializer(plant_inst)
        return Response(serializer.data)

    elif request.method == 'PUT':
        voter = UserVoter(request)
        data = JsonReader.read_body(request)
        if not voter.is_superuser():
            return Response({'error': "Non admin cannot update admin attributes"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PlantationAvgSerializer(plant_inst, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_admin_avg_measurement_index(request):
    """
    get:
    List all plants.
    post:
    Create new plants.
    """
   # voter = UserVoter(request)
   # if not voter.is_superuser():
   #     return Response({'error': "Plant API is not allowed by non admin user"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = PlantationAvgSerializer(PlantationAvg.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonReader.read_body(request)
        serializer = PlantationAvgSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
