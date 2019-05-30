from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import Plantation





@api_view(['GET'])
def api_plant_delete(request, pk):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    try:
        plant_inst = Plantation.objects.get(pk=pk)
    except Plantation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    plant_inst.delete()
    return Response(status.HTTP_202_ACCEPTED)

