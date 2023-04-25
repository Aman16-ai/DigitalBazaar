from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", getUserCart),
    path("getUserCartItems/", getCartItems),
    path("addItemToCart/", addItemToCart),
    path("incrementQuantity/<int:pk>/", incrementCartItem)
]
