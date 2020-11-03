from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    context = {'index': 'true'}
    return render(request, 'customer/index.html', context)


def login(request):
    context = {'login': 'true'}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        context = {'login': 'true'}
        return render(request, 'register.html', context)


def cart(request):
    context = {}
    return render(request, 'customer/cart.html', context)


def contact(request):
    context = {'contact': 'true'}
    return render(request, 'customer/contact.html', context)


def products(request):
    context = {'products': 'true'}
    return render(request, 'customer/products.html', context)


def coupons(request):
    context = {'coupons': 'true'}
    return render(request, 'customer/coupons.html', context)
