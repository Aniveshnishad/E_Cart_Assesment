from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user_data.models import UserTable
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['email', 'password', 'firstName', 'lastName']

    def create(self, validated_data):
        validated_data['email'] = validated_data['email'].lower()
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserTableSerializer, self).create(validated_data)


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['id', 'email', 'firstName', 'lastName']


class AuthTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
