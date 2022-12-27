from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("login/", ObtainAuthToken.as_view(), name="login")
]