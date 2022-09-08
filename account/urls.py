from django.contrib import admin
from django.urls import path,include
from account import views
urlpatterns = [
    path("register/",views.register,name='register'),
    path("register/signup",views.handleSignUp,name="signup"),
    path("login/",views.loginUser,name="loginUser"),
    path("handlelogin",views.handleUserLogin,name="handleUserLogin"),
    path("logout/",views.logoutUser,name="logoutuser")
]