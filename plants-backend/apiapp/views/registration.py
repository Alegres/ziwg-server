from django.core.urlresolvers import reverse
from apiapp.security.voters import UserVoter
from apiapp.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
import json
from apiapp.utils.jsonreader import JsonReader
from apiapp.serializers.user import UserSerializer, PasswordSerializer


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
    data = JsonReader.read_body(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_user_detail(request):

    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "User API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(pk=voter.get_id())
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def api_password_change(request):

    voter = UserVoter(request)
    if not voter.is_logged_in():
        return Response({'error': "User API is not allowed by non logged user"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        serializer = PasswordSerializer(data=request.data)
        user = voter.get()

        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']},
                                status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'New password applied.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
