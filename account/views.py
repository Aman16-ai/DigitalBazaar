from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from account.models import UserProfile
from cart.models import Cart
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registerPage(request):
    return render(request,"account/Signup.html")

def loginPage(request):
    return render(request,"account/login.html")

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
        

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['user_password']
        
        isUserNameNotEmpty = len(username.strip()) > 0
        isPasswordNotEmtpy = len(password.strip()) > 0
        if(isUserNameNotEmpty and isPasswordNotEmtpy):
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return HttpResponse("Failed to login| credentails may be wrong")
        else:
            return HttpResponse("Please enter username and password")
        
    return HttpResponse("Something went wrong")
        
        
def logoutUser(request):
    logout(request)
    return redirect("/")