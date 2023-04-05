from django.contrib import admin
from django.urls import path, include
from .views import *
from .router import router

urlpatterns = [
    path("", getUserCart),
    path("getUserCartItems/", getCartItems),
    path("addItemToCart/",addItemToCart),
    path('', include(router.urls))
]
