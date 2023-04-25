from abc import ABC

from rest_framework import serializers
from cart.models import Cart, CartItem
from product.models import Product
from productApi.serializers import ProductSerializer


class CartSerializers(serializers.ModelSerializer):
    getCartTotal = serializers.ReadOnlyField()
    getCartTotalDiscount = serializers.ReadOnlyField()
    getCartOriginalPrice = serializers.ReadOnlyField()
    getCartTotalItems = serializers.ReadOnlyField()

    class Meta:
        fields = "__all__"
        model = Cart
        depth = True


class CartItemSerializers(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = CartItem


class CartAddItemSerializer(serializers.Serializer):
    # product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    # def create(self, validated_data):
    #     print(self.context['user'])
    #     user_cart = Cart.getUserCart(self.context['user'])
    #     product = Product.objects.get(validated_data['product_id'])
    #     return Cart.addItemToCart(user_cart, product, validated_data['quantity'])
