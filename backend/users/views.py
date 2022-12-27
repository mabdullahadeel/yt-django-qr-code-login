from uuid import uuid4
import datetime
from asgiref.sync import async_to_sync
from django.http import HttpRequest
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserPublicSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from channels.layers import get_channel_layer
from .models import User

TEN_MINUTES_IN_SECONDS = 60 * 10
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


class CodeAuthView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request: HttpRequest, ws_token: str) -> Response:
        ws_cookie = request.COOKIES.get("ws_token")
        if ws_cookie and cache.has_key(ws_cookie):
            return Response({"ws_token": ws_cookie}, status=status.HTTP_200_OK)
        
        ws_token = uuid4().hex[0:6]
        while cache.has_key(ws_token):
            ws_token = uuid4().hex[0:6]
        
        cache.set(ws_token, '', timeout=TEN_MINUTES_IN_SECONDS)
        response = Response({"ws_token": ws_token}, status=status.HTTP_200_OK)
        expires_in = datetime.datetime.now() + datetime.timedelta(seconds=TEN_MINUTES_IN_SECONDS)
        response.set_cookie("ws_token", ws_token, expires=expires_in, httponly=True, path=request.path)
        return response

class CodeAuthLoginView(APIView):
    def post(self, request: HttpRequest) -> Response:
        ws_token = request.data["ws_token"]
        token = cache.get(ws_token)
        channel_name = cache.get(ws_token)
        if token and channel_name:
            auth_token = Token.objects.get(user=request.user).key
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.send)(channel_name, {
                "type": "send.token",
                "token": auth_token
            })
            cache.delete(ws_token)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


