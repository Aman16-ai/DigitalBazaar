from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
@api_view(["GET"])
def getAllProducts(request):
    if request.method == 'GET':
        if 'category' in request.GET:
            user_category = request.GET['category']
            products = Product.getProductByCategory(user_category)
            return Response({"products":ProductSerializer(products,many=True).data})

        else :
            allProducts = Product.objects.all()
            ser = ProductSerializer(allProducts,many=True)
            return Response({"allProducts":ser.data})
    return Response({"message":"all products"})


@api_view(["GET"])
def getAllCategories(request):
    if request.method == 'GET':
        allCategories = Category.objects.all()
        ser = CategorySerializer(allCategories,many=True)
        return Response({"allCategories":ser.data})

    return Response({"message":"category api"})


@api_view(["GET"])
def getProductByCategory(request):
    if request.method == 'GET':
        user_category = request.method.GET['category']
        print(user_category)

    return Response({"message":"category api"})