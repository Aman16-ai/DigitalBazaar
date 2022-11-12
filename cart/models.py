from datetime import datetime
from tkinter import CASCADE
from warnings import catch_warnings
from django.db import models
from django.db.models import Q
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
        userCartItems = CartItem.objects.filter(cart = self)
        total = 0
        for item in userCartItems:
            total += item.product.getFinalPrice * item.quantity
            
        return total
    
    @property
    def getCartTotalDiscout(self):
        userCartItems = CartItem.objects.filter(cart = self)
        totalDiscount = 0
        for item in userCartItems:
            totalDiscount += item.product.getDiscountPrice() * item.quantity
            
        return totalDiscount
    
    @property
    def getCartOriginalPrice(self):
        userCartItems = CartItem.objects.filter(cart = self)
        total = 0
        for item in userCartItems:
            total += item.product.price * item.quantity
            
        return total
     
    @property
    def getCartTotalItems(self):
        userCartItem = CartItem.objects.filter(cart = self)
        count = 0
        for item in userCartItem:
            count += item.quantity
        return count

    def __str__(self):
        return f"{self.user.user.username} cart"
    
    
    @staticmethod
    def getAllCartItemsOfCurrentUser(user):
        try:
            user_cart = Cart.getUserCart(user)
            allcartitems = CartItem.objects.filter(cart = user_cart)
            print(allcartitems)
            return allcartitems
        except Exception as e:
            print(e)
    
    def addItemToCart(self,product,quantity):
        try:
            cartItem = CartItem.objects.filter(Q(cart=self) & Q(product = product))
            if len(cartItem) != 0:
                print("Already exsits")
                print(cartItem)
                cartItem[0].quantity += 1
                cartItem[0].save()
            else:
                 cartItem = CartItem(cart = self,product = product,quantity = quantity)
                 cartItem.save()
                 self.quantity += 1;
                 self.save()
            return True
        except Exception as e:
            print(e)
            return False
            
    

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    created_at = models.DateField(default=datetime.now())
    
    def __str__(self):
        return f"cart item : {self.product.title}"
    
        
    