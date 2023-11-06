from rest_framework import serializers
from .models import Order, Transaction
from cart.models import CartItem
from account.models import Address, UserProfile
from api.serializers import UserProfileSerializer
from .service.razorpayService import RazorPayClient
class OrderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    get_total = serializers.ReadOnlyField()
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

        razropay_client = RazorPayClient()
        result = razropay_client.create_order(order.get_total)
        print(result)
        order.online_payment_order_id = result['id']
        order.save()
        return order
    

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
    
    def create(self, validated_data):
        rz_client = RazorPayClient()
        amount = validated_data.pop('amount')
        result = rz_client.verify_payment_signature(**validated_data)
        print('result ---->',result)
        transcation = Transaction(**validated_data,amount = amount)
        return transcation

