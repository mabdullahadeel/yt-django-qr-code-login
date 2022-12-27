from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views as user_views

urlpatterns = [
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("register/", user_views.UserCreateView.as_view(), name="register"),
    path("me/", user_views.UserMeView.as_view(), name="me"),
]