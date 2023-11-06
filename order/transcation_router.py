from rest_framework.routers import SimpleRouter
from .views import TranscationViewSet
tran_router = SimpleRouter()
tran_router.register("transcation/",TranscationViewSet,basename="transcation")