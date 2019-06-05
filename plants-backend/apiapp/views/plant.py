from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import Plantation, User2Plantation
from apiapp.serializers.plant import PlantationSerializer
from apiapp.utils.jsonreader import JsonReader
from apiapp.security.voters import UserVoter


@api_view(['GET', 'PUT'])
def api_plant_detail(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """

    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "Plant API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    try:
        plant_inst = Plantation.objects.get(pk=pk)
    except Plantation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantationSerializer(plant_inst)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JsonReader.read_body(request)
        serializer = PlantationSerializer(plant_inst, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_admin_plant_index(request):
    """
    get:
    List all plants.
    post:
    Create new plants.
    """
    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "Plant API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        plants = User2Plantation.objects.filter(id_user=voter.get_id())
        serializer = PlantationSerializer(
            Plantation.objects.filter(pk__in=plants), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonReader.read_body(request)
        serializer = PlantationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
