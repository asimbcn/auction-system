from django.shortcuts import render, redirect
from .models import *
from Administrator.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from .utils import check_permission


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'index': 'true', 'products': products}
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
            try:
                customer = Customer.objects.get(user=user)
                if customer.admin == True:
                    return redirect('adminSelect')
            except:
                messages.info(request, 'User not found')

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


@login_required(login_url='login')
def adminSelect(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    if request.method == 'GET' and 'redir' in request.GET:
        if request.GET['redir'] == 'admin':
            return redirect('adminIndex')
        elif request.GET['redir'] == 'home':
            return redirect('home')
        else:
            return redirect('logout')

    context = {}
    return render(request, 'redirect.html', context)


def cart(request):
    context = {}
    return render(request, 'customer/cart.html', context)


def viewProduct(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'customer/view.html', context)


def completeProduct(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'customer/all.html', context)


@login_required(login_url='login')
def wishlist(request):
    context = {'wishlist': 'true'}
    return render(request, 'customer/wishlist.html', context)


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('home')
