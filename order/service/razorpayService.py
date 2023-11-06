import razorpay
from rest_framework.serializers import ValidationError
from rest_framework import status
from django.conf import settings
class RazorPayClient:

    def __init__(self) -> None:
        self.client = razorpay.Client(auth=("rzp_test_vy2VJ9K37eJMD9","GPpLAlEmAxIyWRGyjDRbk1kn"))

    
    def create_order(self,amount,currency="INR"):
        data = {
            "amount": amount*100,
            "currency":currency 
        }

        try:
            return self.client.order.create(data=data)
        except Exception as e:
            raise ValidationError(
                {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": e
                }
            )
        
    def verify_payment_signature(self, order_id, payment_id, signature):
        try:
            self.verify_signature = self.client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
            return self.verify_signature
        except Exception as e:
            raise ValidationError(
                {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": e
                }
            )