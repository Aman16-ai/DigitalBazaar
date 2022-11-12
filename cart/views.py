from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from account.models import UserProfile

from cart.models import Cart, CartItem
from product.models import Product

# Create your views here.
def mycart(request):
    #fetching all cartitems of current user
   
    allitem = Cart.getAllCartItemsOfCurrentUser(request.user)
    userCart = Cart.getUserCart(request.user)
    print(f"Cart Total : {userCart.getCartTotal} Total Items : {userCart.getCartTotalItems}")
    for item in allitem:
        print(f"Product : {item.product.title[:5]} , Price :{item.product.getFinalPrice} and Quantity : {item.quantity}")
    return render(request,"cart/index.html",{"cart":userCart})

def addToCart(request,pk):
    cart = Cart.getUserCart(request.user)
    product = Product.objects.get(pk = pk)
    print(cart)
    result = cart.addItemToCart(product=product,quantity=1)
    print(result)
    if result:
        return redirect("/")
    return HttpResponse("something went wrong")