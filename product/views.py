from django.shortcuts import render
from django.http import HttpResponse

from product.models import Product
# Create your views here.
def index(request,pk):
    product = Product.objects.get(pk = pk)
    context = {'product':product}
    return render(request,"product/index.html",context)