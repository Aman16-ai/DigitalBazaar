from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def mycart(request):
    return HttpResponse("this is my chart")