from django.contrib import admin
from .models import Order,Transaction
# Register your models here.
admin.site.register((Order,Transaction))