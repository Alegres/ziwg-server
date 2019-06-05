from apiapp.security.voters import UserVoter
from apiapp.utils.jsonreader import JsonReader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import PlantationPreset
from apiapp.serializers.preset import PresetSerializer
from apiapp.serializers.user import User


@api_view(['GET', 'PUT'])
def api_preset_detail(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "Preset API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    try:
        preset_id = PlantationPreset.objects.get(pk=pk)
    except PlantationPreset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PresetSerializer(preset_id)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JsonReader.read_body(request)
        serializer = PresetSerializer(preset_id, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_admin_preset_index(request):
    """
    get:
    List all plants.
    post:
    Create new plants.
    """
    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "Preset API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = PresetSerializer(
            PlantationPreset.objects.filter(id_user=voter.get_id()), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonReader.read_body(request)
        serializer = PresetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
