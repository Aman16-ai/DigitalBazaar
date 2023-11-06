from rest_framework.routers import SimpleRouter
from .views import OrderViewSet,TranscationViewSet
order_router = SimpleRouter()
order_router.register("userOrder",OrderViewSet)
order_router.register("transcation",TranscationViewSet,basename="transcation")
