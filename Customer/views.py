from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm


# Create your views here.
def index(request):
    context = {'index': 'true'}
    return render(request, 'customer/index.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        pass

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password Incorrect')

    context = {'login': 'true'}
    return render(request, 'login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        pass

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.info(request, 'Registration Error, Try Again')

    context = {'login': 'true', 'form': form}
    return render(request, 'register.html', context)


def cart(request):
    context = {}
    return render(request, 'customer/cart.html', context)


def coupons(request):
    context = {'coupons': 'true'}
    return render(request, 'customer/coupons.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')
