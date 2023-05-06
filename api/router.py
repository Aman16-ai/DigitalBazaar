from rest_framework.routers import SimpleRouter
from .views import AddressViewSet
addres_router = SimpleRouter()
addres_router.register("userAddress",AddressViewSet,basename="userAddress")