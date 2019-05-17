from apiapp.security.voters import UserVoter
from apiapp.utils.jsonreader import JsonReader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import User2Plantation
from apiapp.serializers.preset import User2PlantationSerializer
from apiapp.serializers.user import User


@api_view(['GET', 'PUT'])
def api_user2plantation_detail(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    try:
        preset_id = User2Plantation.objects.get(id_user=pk)
    except User2Plantation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = User2PlantationSerializer(preset_id)
        return Response(serializer.data)

    elif request.method == 'PUT':
        voter = UserVoter(request)
        data = JsonReader.read_body(request)
        if not voter.is_superuser():
            return Response({'error': "Non admin cannot update preset"}, status=status.HTTP_403_FORBIDDEN)
        serializer = User2PlantationSerializer(preset_id, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_admin_user2plantation_index(request):
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
        serializer = User2PlantationSerializer(
            User2Plantation.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JsonReader.read_body(request)
        serializer = User2PlantationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
