from rest_framework import serializers
from cart.models import Cart,CartItem

class CartSerializers(serializers.ModelSerializer):
    getCartTotal = serializers.ReadOnlyField()
    getCartTotalDiscount = serializers.ReadOnlyField()
    getCartOriginalPrice = serializers.ReadOnlyField()
    getCartTotalItems = serializers.ReadOnlyField()
    class Meta:
        fields = "__all__"
        model = Cart
        depth = True