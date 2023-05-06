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
    
    
    @staticmethod
    def registerUser(username,firstname,lastname,email,password,phone_no,age,gender):
        user = User.objects.create_user(username = username,email=email,password = password)
        user.first_name = firstname
        user.last_name = lastname
        if user is not None:
            userProfile = UserProfile(user = user,phone_no = phone_no,age = age,gender = gender)
            userProfile.save()
            user.save()
            if userProfile is not None:
               return userProfile
                
        return None
    
    def __str__(self):
        return self.user.username
    

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    landmark = models.CharField(max_length=50)
    pincode = models.PositiveIntegerField()
    

    