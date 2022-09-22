from tkinter import EW
from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    products_with_highest_discount = products[0]
    for p in products:
        if p.discount >= products_with_highest_discount.discount:
            products_with_highest_discount = p
            
    
            
    print(products_with_highest_discount)
    print(Product.getDiscountedPrice())
    context = {"bestDeal":products_with_highest_discount,"discounted_products":Product.getDiscountedPrice()}
    return render(request,'index.html',context)