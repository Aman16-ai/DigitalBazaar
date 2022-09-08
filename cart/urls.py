from django.contrib import admin
from django.urls import path,include
from account import views
urlpatterns = [
    path("register/",views.register,name='register')
]