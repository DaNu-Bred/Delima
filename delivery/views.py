from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    return render(request, "delivery/home.html")

def ch1 (request):
    return render(request, "delivery/ch1.html")

def ch2 (request):
    return render(request, "delivery/ch2.html")
