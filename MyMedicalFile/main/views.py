from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.



def index(request : HttpRequest):
    return render(request, "main/index.html")

def about_us(request : HttpRequest):
    return render(request, "main/about_us.html")