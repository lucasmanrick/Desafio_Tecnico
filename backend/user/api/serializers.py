from rest_framework import serializers
from user import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'password','first_name', 'last_name']