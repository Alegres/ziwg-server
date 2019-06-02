from django.core.urlresolvers import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
import json
from apiapp.utils.jsonreader import JsonReader


@api_view(['POST'])
def api_login(request):
    """
    post:
    This view is called through API POST with a json body like so:

    {
        "useremail": "admin",
        "password": "admin"
    }

    :param request:
    :return:
    """
    data = JsonReader.read_body(request)

    response_login = requests.post(
        request.build_absolute_uri(reverse('obtain_jwt_token')),
        data=data
    )
    response_login_dict = json.loads(response_login.content)
    return Response(response_login_dict, response_login.status_code)


@api_view(['POST'])
def api_register(request):

    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
