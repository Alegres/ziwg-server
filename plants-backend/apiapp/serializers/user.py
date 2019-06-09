from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apiapp.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        required=True, allow_blank=False, max_length=100, validators=[
            UniqueValidator(queryset=User.objects.all())
        ])
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.CharField(
        required=True, allow_blank=False, max_length=100)
    first_name = serializers.CharField(
        required=True, max_length=30, allow_blank=False)
    last_name = serializers.CharField(
        required=True, max_length=150, allow_blank=True)
    phone_number = serializers.IntegerField(required=True, allow_null=False)
    is_staff = serializers.BooleanField(required=False, default=False)
    is_superuser = serializers.BooleanField(required=False, default=False)

    def create(self, data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        instance = User.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            is_staff=data.get('is_staff'),
            is_superuser=data.get('is_superuser'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone_number=data.get('phone_number'),
        )
        instance.set_password(data.get('password'))
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = data.get('username', instance.username)
        instance.email = data.get('email', instance.email)
        instance.is_staff = data.get('is_staff', instance.is_staff)
        instance.is_superuser = data.get('is_superuser', instance.is_superuser)
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.phone_number = data.get('phone_number', instance.phone_number)
        instance.set_password(data.get('password'))
        instance.save()
        return instance


class UserSettingsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=False, max_length=100, validators=[
        UniqueValidator(queryset=User.objects.all())
    ])
    email = serializers.CharField(
        required=False, allow_blank=False, max_length=100)
    first_name = serializers.CharField(
        required=False, max_length=30, allow_blank=False)
    last_name = serializers.CharField(
        required=False, max_length=150, allow_blank=True)
    phone_number = serializers.IntegerField(required=False, allow_null=False)

    def update(self, instance, data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = data.get('username', instance.username)
        instance.email = data.get('email', instance.email)
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.phone_number = data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
