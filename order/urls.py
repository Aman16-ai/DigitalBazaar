from django.urls import path,include
from .router import order_router
urlpatterns = [
    path("",include(order_router.urls))
]
