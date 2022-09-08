from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gender_choice = (
    ('M',"Male"),
    ('F',"Female")
)

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    phone_no = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=gender_choice,max_length=6)
    

    