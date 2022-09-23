from django.contrib import admin
from django.urls import path,include
from cart import views
urlpatterns = [
    path("",views.mycart,name='mycart'),
    path("addToCart/<str:pk>",views.addToCart,name="")
]