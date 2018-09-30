from rest_framework import serializers
from .model import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'birthday', 'email', 'address')