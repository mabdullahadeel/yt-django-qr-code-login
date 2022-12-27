from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/code_auth/(?P<ws_token>\w+)/$', consumers.CodeAuthConsumer.as_asgi())
]