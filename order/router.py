from rest_framework.routers import SimpleRouter
from .views import OrderViewSet
order_router = SimpleRouter()
order_router.register("",OrderViewSet)
