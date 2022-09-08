from django.contrib import admin
from django.urls import path,include
from account import views
urlpatterns = [
    path("register/",views.registerPage,name='register'),
    path("register/signup",views.handleSignUp,name="signup"),
    path("login/",views.loginPage,name="loginPage"),
    path("login/handlelogin",views.handlelogin,name="handlelogin"),
    path("logout/",views.logoutUser,name="logoutUser")
    
]