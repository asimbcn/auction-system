from django.shortcuts import render, redirect
from .models import *
from Administrator.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from .utils import *
import datetime


# Create your views here.
def index(request):
    if checkProd():
        products = Product.objects.all()
        context = {'index': 'true', 'products': products}
        return render(request, 'customer/index.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

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

    context = {'route': 'true'}
    return render(request, 'redirect.html', context)


@login_required(login_url='login')
def editUser(request, pk):
    customer = Customer.objects.get(id=pk)
    user = customer.user

    if request.method == 'POST':
        if checkUserEdit(request, pk):
            if saveInfo(request, pk):
                return redirect(Userprofile, user=user)

    context = {'profile': 'true', 'user': user}
    return render(request, 'customer/editUser.html', context)


def cart(request):
    context = {}
    return render(request, 'customer/cart.html', context)


def viewProduct(request, slug):
    product = Product.objects.get(slug=slug)
    if checkWishlist(request, slug) == True:
        wishlist = True
    else:
        wishlist = False

    if product.status == False:
        return redirect('home')
    context = {'product': product, 'data': wishlist}
    return render(request, 'customer/view.html', context)


def completeProduct(request, slug):
    product = Product.objects.get(slug=slug)
    if product.status == False:
        return redirect('home')
    context = {'product': product}
    return render(request, 'customer/all.html', context)


@login_required(login_url='login')
def wishlist(request):
    wishlist = WishList.objects.filter(customer=request.user.customer)
    context = {'wishlist': 'true', 'data': wishlist}
    return render(request, 'customer/wishlist.html', context)


@login_required(login_url='login')
def addWishlist(request, slug):
    if checkWishlist(request, slug) == True:
        try:
            product = Product.objects.get(slug=slug)
            customer = Customer.objects.get(user=request.user)
            WishList.objects.create(customer=customer, product=product)
        except:
            pass

    return redirect(viewProduct, slug=slug)


@login_required(login_url='login')
def removeWishlist(request, slug):
    if checkWishlist(request, slug) == False:
        try:
            product = Product.objects.get(slug=slug)
            wishlist = WishList.objects.get(product=product)
            wishlist.delete()
        except:
            pass

    return redirect(viewProduct, slug=slug)


@login_required(login_url='login')
def editPhoto(request, pk):
    profile = getProfile(request, pk)
    if request.method == 'POST':
        profile.image = request.FILES['image']
        try:
            profile.save()
        except:
            pass

    return redirect(Userprofile, user=request.user)


@login_required(login_url='login')
def Userprofile(request, user):
    if str(request.user) != str(user):
        customer = getProfile(request, user=user)
        if customer == False:
            return redirect(Userprofile, user=request.user)

        shipping = getShipping(request, user)
        currentUser = False

    else:
        customer = getProfile(request)
        shipping = getShipping(request)
        currentUser = True
    # transaction_id = int(datetime.datetime.now().timestamp())
    context = {
        'profile': 'true',
        'customer': customer,
        'shipping': shipping,
        'user': user,
        'currentUser': currentUser
    }
    return render(request, 'customer/profile.html', context)


@login_required(login_url='login')
def editShipping(request, pk):
    customer = Customer.objects.get(id=pk)
    user = customer.user
    shipping = ShippingAddress.objects.get(customer=customer)

    if request.method == 'POST':
        address, city, state, zipcode = checkShipping(request, shipping)
        shipping.address = address
        shipping.city = city
        shipping.state = state
        shipping.zipcode = zipcode
        shipping.edit = False
        try:
            shipping.save()
            return redirect(Userprofile, user=user)
        except:
            messages.info(request, 'Something Went Wrong!')

    context = {'profile': 'true', 'shipping': shipping}
    return render(request, 'customer/shipping.html', context)


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def bidderInfo(request, slug):
    product = Product.objects.get(slug=slug)
    bider = Bid.objects.filter(product=product)
    bidders = sorted(bider, key=lambda bid: bid.date_created, reverse=True)
    context = {'bidders': bidders, 'product': product}
    return render(request, 'customer/bid.html', context)


@login_required(login_url='login')
def placeBid(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        user_amount = request.POST['bidamount']
        if validBid(product, user_amount):
            if bidAmountCheck(user_amount, product):
                if biddingUser(request.user.customer, product):
                    setHighestBidder(product, user_amount,
                                     request.user.customer)
                else:
                    messages.info(request,
                                  'You are already the highest bidder')
            else:
                messages.info(request, 'Bid Amount is not Valid')
        else:
            messages.info(request, 'Not a Valid Bid')

        return redirect(viewProduct, slug=slug)
