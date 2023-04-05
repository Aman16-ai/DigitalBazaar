from rest_framework.routers import SimpleRouter
from .views import CartItemViewSet

router = SimpleRouter()
router.register("cartItem", CartItemViewSet,basename="cartItem")
