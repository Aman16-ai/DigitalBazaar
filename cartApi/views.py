from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializers, CartItemSerializers, CartAddItemSerializer
from cart.models import Cart, CartItem
from product.models import Product


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserCart(request):
    user_cart = Cart.getUserCart(request.user)
    ser = CartSerializers(user_cart)
    return Response({"user_cart": ser.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCartItems(request):
    try:
        allItems = Cart.getAllCartItemsOfCurrentUser(request.user)
        ser = CartItemSerializers(allItems, many=True)
        return Response({"Result": ser.data})
    except Exception as e:
        return Response({"error": "some internal server error"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addItemToCart(request):
    try:
        productId = request.data['product_id']
        quantity = request.data['quantity']
        user_cart = Cart.getUserCart(request.user)
        product = Product.objects.get(pk=productId)
        # result = Cart.addItemToCart(user_cart, product, quantity)
        result = user_cart.addItemToCart(product=product, quantity=quantity)
        print('running inside additem view api', type(result))
        if result != None:
            # ser = CartItemSerializers(result)
            # print(ser.data)
            return Response({"Response": 'added'})

        return Response({"Response": "Failed to add item to cart"})
        # serializer = CartAddItemSerializer(data=request.data,context={'user':request})
        # if serializer.is_valid(raise_exception=True):
        #     result = serializer.save()
        #     return Response({"Response":result},status=200)
        # return Response({"Response": serializer.error_messages},status=501)
    except Exception as e:
        return Response({"error": "some internal server error"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def incrementCartItem(request, pk):
    try:
        if request.method == 'POST':
            ser = CartAddItemSerializer(data=request.data)
            if ser.is_valid(raise_exception=True):
                cart_item = CartItem.objects.get(pk=pk)
                user_cart = Cart.getUserCart(request.user)
                print("Quanity", request.data['quantity'])
                result = cart_item.incrementItemQuantity(
                    user_cart, ser['quantity'].value)
                if result is not None:
                    ser = CartItemSerializers(result,many=False)
                    return Response({"status":True,"Reponse":ser.data})
                return Response({"status":False,"Response": result})
        return Response({"Error": "Method not valid"})
    except Exception as e:
        return Response({"Error": "Something went wrong"})
