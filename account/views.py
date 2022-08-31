from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,"account/Signup.html")