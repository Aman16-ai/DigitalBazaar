from rest_framework import serializers
from .models import Order
from cart.models import CartItem
from account.models import Address, UserProfile
from api.serializers import UserProfileSerializer
class OrderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        exclude =('status',)
        model = Order

    def create(self, validated_data):
        
        user = self.context['request'].user
        order = Order(user = UserProfile.objects.get(user = user),address = validated_data['address'])
        order.save()

        for item in validated_data['items']:
            # TODO: add a validation that item is already ordered or not
            item.status = "ORDERED"
            item.save()
            order.items.add(item)
        return order
    