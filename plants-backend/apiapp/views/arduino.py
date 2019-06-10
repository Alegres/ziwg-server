from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import Plantation, Plantation2Arduino, PlantationPreset
from apiapp.serializers.preset import PresetSerializer
from apiapp.utils.jsonreader import JsonReader
from apiapp.security.voters import UserVoter


@api_view(['GET', 'PUT'])
def arduino_data(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """

    try:
        plantation2Arduino = Plantation2Arduino.objects.get(id_arduino=pk)
    except Plantation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PresetSerializer(PlantationPreset.objects.get(
            pk=plantation2Arduino.id_plantation.id_preset.id))
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_admin_arduino_index(request):
    """
    get:
    List all plants.
    post:
    Create new plants.
    """
    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "Plant API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    # if request.method == 'GET':
     #   plantation2Arduino = Plantation2Arduino.objects.get(id_arduino=pk)
     #   serializer = PresetSerializer(PlantationPreset.objects.get(pk=plantation2Arduino.id_plantation.idpreset))
     #   return Response(serializer.data)
