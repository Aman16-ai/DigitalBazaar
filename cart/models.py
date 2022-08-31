from datetime import datetime
from tkinter import CASCADE
from django.db import models

from account.models import UserProfile
from product.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=0)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.user.username} cart"
    

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateField(default=datetime.now())
    