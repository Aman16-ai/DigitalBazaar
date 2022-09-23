from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from account.models import UserProfile

from cart.models import Cart, CartItem
from product.models import Product

# Create your views here.
def mycart(request):
    return HttpResponse("this is my chart")

def addToCart(request,pk):
    cart = Cart.getUserCart(request.user)
    product = Product.objects.get(pk = pk)
    print(cart)
    result = CartItem.addItemToCart(cart = cart,product=product,quantity=1)
    if result:
        redirect("/")
    return HttpResponse("something went wrong")