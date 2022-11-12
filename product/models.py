from datetime import datetime
from math import prod
from pyexpat import model
from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="category_img")
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    content = FroalaField(blank=True, null=True)
    product_img = models.ImageField(upload_to="product_images")
    price = models.PositiveIntegerField()
    discount = models.FloatField(null=True,blank=True,default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default="other")
    stock = models.PositiveIntegerField()
    created_at = models.DateField(default = datetime.now())
    
    
    @property
    def getFinalPrice(self):
        return round(self.price - self.getDiscountPrice())
            
    @staticmethod
    def getDiscountedProduct():
        product = Product.objects.order_by("-discount").all()
        productwithdiscount = [p for p in product if p.discount > 0]
        return productwithdiscount
    
    def getDiscountPrice(self):
        dis_amount = (self.discount/100) * self.price
        return dis_amount
    
    def __str__(self):
        return self.title