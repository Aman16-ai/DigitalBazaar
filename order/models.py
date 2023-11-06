from django.db import models

from account.models import Address, UserProfile
from cart.models import CartItem

# Create your models here.
STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('PROCESSING', 'PROCESSING'),
        ('SHIPPED', 'SHIPPED'),
        ('DELIVERED', 'DELIVERED'),
    )
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    online_payment_order_id = models.CharField(max_length=250,null=True,blank=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="order_user")
    items = models.ManyToManyField(CartItem)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=20,default='PENDING')
    address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name="order_address")

    def __str__(self) -> str:
        return "Order : " + self.user.user.username
    @property
    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.product.getFinalPrice * item.quantity
        return total

class Transaction(models.Model):
    payment_id = models.CharField(max_length=200, verbose_name="Payment ID")
    order_id = models.CharField(max_length=200, verbose_name="Order ID")
    signature = models.CharField(max_length=500, verbose_name="Signature", blank=True, null=True)
    amount = models.IntegerField(verbose_name="Amount")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)