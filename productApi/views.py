from rest_framework import viewsets
from rest_framework.response import Response
from product.models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from django_filters import rest_framework as filters

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = {
        'category__name':['exact'],
        'title' : ['exact']
    }

