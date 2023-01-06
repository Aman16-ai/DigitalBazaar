from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializers
from cart.models import Cart

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserCart(request):
    user_cart = Cart.getUserCart(request.user)
    ser = CartSerializers(user_cart)
    return Response({"user_cart":ser.data})
