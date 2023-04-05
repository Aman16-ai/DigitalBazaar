from abc import ABC

from rest_framework import serializers
from cart.models import Cart, CartItem


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
    class Meta:
        fields = "__all__"
        model = CartItem
        depth = True


class CartAddItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


