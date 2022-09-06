from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from account.models import UserProfile
from cart.models import Cart

# Create your views here.

def register(request):
    return render(request,"account/Signup.html")

def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['Username']
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        email = request.POST['email']
        password = request.POST['pass']
        phoneNo = request.POST['PhoneNo']
        age = request.POST['Age']
        gender = request.POST['Gender']
        
        userProfile = UserProfile.registerUser(username=username,firstname=firstname,lastname=lastname,email=email,password=password,phone_no=phoneNo,age=age,gender=gender)
        
        if userProfile is not None:
            isUserCartCreated = Cart.createCart(user = userProfile)
            if(isUserCartCreated):
                return redirect("/")
            else:
                return HttpResponse("Failed to create user cart")
        else:
            return HttpResponse("Failed to register user")