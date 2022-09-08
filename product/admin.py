from ast import Sub
from django.contrib import admin
from product.models import Product,Category,SubCategory
# Register your models here.
admin.site.register((Product,Category,SubCategory))