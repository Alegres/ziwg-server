from apiapp.security.voters import UserVoter
from apiapp.utils.jsonreader import JsonReader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import Plantation2Arduino
from apiapp.serializers.preset import Plantation2ArduinoSerializer
from apiapp.serializers.user import User


@api_view(['GET', 'PUT'])
def api_plantation2arduino_detail(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    try:
        preset_id = Plantation2Arduino.objects.get(id_plantation=pk)
    except Plantation2Arduino.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Plantation2ArduinoSerializer(preset_id)
        return Response(serializer.data)

    elif request.method == 'PUT':
        voter = UserVoter(request)
        data = JsonReader.read_body(request)
        if not voter.is_superuser():
            return Response({'error': "Non admin cannot update preset"}, status=status.HTTP_403_FORBIDDEN)
        serializer = Plantation2ArduinoSerializer(preset_id, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_admin_plantation2arduino_index(request):
    """
    get:
    List all plants.
    post:
    Create new plants.
    """
    voter = UserVoter(request)
    if not voter.is_superuser():
        return Response({'error': "Plant API is not allowed by non admin user"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = Plantation2ArduinoSerializer(
            Plantation2Arduino.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonReader.read_body(request)
        serializer = Plantation2ArduinoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
