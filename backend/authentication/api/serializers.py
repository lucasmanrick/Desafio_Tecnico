from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
from uuid import uuid4

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "created_at"]
        read_only_fields = ["id", "created_at"]
    def create(self, validated_data):
        validated_data["username"] = str(uuid4())
        user = User.objects.create_user(**validated_data)
        return user
    

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email", "first_name", "last_name", "created_at"]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data  
        return data