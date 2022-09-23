from tkinter import EW
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from product.models import Category, Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    mensCategory = Category.objects.get(name="Men's wear")
    mens_wear = Product.objects.filter(category = mensCategory)
    products_with_highest_discount = products[0]
    for p in products:
        if p.discount >= products_with_highest_discount.discount:
            products_with_highest_discount = p
            
    context = {"bestDeal":products_with_highest_discount,"discounted_products":Product.getDiscountedProduct(),"mens":mens_wear}
    return render(request,'index.html',context)