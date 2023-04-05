from rest_framework.routers import SimpleRouter
from .views import ProductViewSet,CategoryViewSet
router = SimpleRouter()
router.register('categories',CategoryViewSet,basename="categories")
router.register('',ProductViewSet)
