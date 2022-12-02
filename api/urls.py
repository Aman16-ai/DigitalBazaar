from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("account/register",register,name='register_api'),
    path("account/getUser",getUser,name="get_user"),
    path("account/login",loginUser,name="login_user")
]