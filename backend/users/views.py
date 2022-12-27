from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserPublicSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import User


class UserMeView(APIView):
    def get(self, request: HttpRequest) -> Response:
        user = UserPublicSerializer(request.user).data
        data = {
            "user": user
        }
        return Response(data=data, status=status.HTTP_200_OK)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request: HttpRequest, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = User.objects.get(username=serializer.data["username"])
        token = Token.objects.create(user=user).key
        return Response({"token": token}, status=status.HTTP_201_CREATED, headers=headers)
        

