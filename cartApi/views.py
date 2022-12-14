from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializers,CartItemSerializers
from cart.models import Cart,CartItem
from product.models import Product

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserCart(request):
    user_cart = Cart.getUserCart(request.user)
    ser = CartSerializers(user_cart)
    return Response({"user_cart":ser.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCartItems(request):
    try:
        allItems = Cart.getAllCartItemsOfCurrentUser(request.user)
        ser = CartItemSerializers(allItems,many=True)
        return Response({"Result":ser.data})
    except Exception as e:
        return Response({"error":"some internal server error"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addItemToCart(request):
    try:
        productId = request.data['product_id']
        quantity = request.data['quantity']
        user_cart = Cart.getUserCart(request.user)
        product = Product.objects.get(pk = productId)
        result = Cart.addItemToCart(user_cart,product,quantity)
        return Response({"Result":result})
    except Exception as e:
        return Response({"error":"some internal server error"})