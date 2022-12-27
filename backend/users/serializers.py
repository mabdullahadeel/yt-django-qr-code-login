from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "is_superuser", "date_joined", "groups", "user_permissions")
        

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=45)
    
    class Meta:
        model: User
        fields: list[str] = ["email", "username", "password"]
        
    def create(self, validated_data: dict) -> User:
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)