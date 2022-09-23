from datetime import datetime
from tkinter import CASCADE
from warnings import catch_warnings
from django.db import models

from account.models import UserProfile
from product.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=0)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    
    

    
    @staticmethod
    def createCart(user):
        cart = Cart(user = user,quantity = 0)
        if cart is not None:
             cart.save()
             return True
        return False
        
    
    @staticmethod
    def getUserCart(user):
        userProfile = UserProfile.objects.get(user = user)
        return Cart.objects.get(user = userProfile)
    
    @property
    def getCartTotal(self):
        userCart = CartItem.objects.filter(cart = self)
        total = 0;
        for item in userCart:
            total += item.product.getFinalPrice
            
        return total
     
    def __str__(self):
        return f"{self.user.user.username} cart"
    

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateField(default=datetime.now())
    
    @staticmethod
    def addItemToCart(cart,product,quantity):
        try:
            result = CartItem(cart = cart,product = product,quantity=quantity)
            result.save()
            return True
        except Exception as err:
            print(err)
            return False
        
    