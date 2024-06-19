from django.shortcuts import render, redirect
from django.http import HttpResponse
import paypalrestsdk
from django.conf import settings

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')

def calendario(request):
    return render(request, 'app/calendario.html')

def carrito(request):
    return render(request, 'app/carrito.html')



       
