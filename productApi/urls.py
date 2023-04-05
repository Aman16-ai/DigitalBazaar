from django.contrib import admin
from django.urls import path,include
from .views import *
from .routers import router
urlpatterns = [
    path("",include(router.urls)),
]