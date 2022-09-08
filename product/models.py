from datetime import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="category_img")
    
    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="sub_category_img")
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    product_img = models.ImageField(upload_to="product_images")
    price = models.PositiveIntegerField()
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=0)
    stock = models.PositiveIntegerField()
    created_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.title