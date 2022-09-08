from datetime import datetime
from pyexpat import model
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="category_img")
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    product_img = models.ImageField(upload_to="product_images")
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default="other")
    stock = models.PositiveIntegerField()
    created_at = models.DateField(default = datetime.now())
    
    def __str__(self):
        return self.title