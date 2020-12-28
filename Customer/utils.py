from .models import *
from Administrator.models import *
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib import messages
import re
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email


def check_permission(request):
    if request.user.customer.admin == False:
        return {'status': False}
    elif request.user.customer.admin == True:
        return {'status': True}
    else:
        return {'status': False}


def getProduct(request):

    try:
        allProd = Product.objects.all()
    except:
        allProd = ''

    try:
        activeProd = Product.objects.filter(status=True)
    except:
        activeProd = ''

    try:
        inactiveProd = Product.objects.filter(status=False)
    except:
        inactiveProd = ''

    return {
        'allProd': allProd,
        'activeProd': activeProd,
        'inactiveProd': inactiveProd
    }


def getCoupon(request):

    try:
        allCoup = Coupon.objects.all()
    except:
        allCoup = ''

    try:
        activeCoup = Coupon.objects.filter(active=True)
    except:
        activeCoup = ''

    try:
        inactiveCoup = Coupon.objects.filter(active=False)
    except:
        inactiveCoup = ''

    return {
        'allCoup': allCoup,
        'activeCoup': activeCoup,
        'inactiveCoup': inactiveCoup
    }


def getProfile(request, pk='None', user='NoOne'):
    if pk != 'None':
        customer = Customer.objects.get(id=pk)
        return customer
    elif user != 'NoOne':
        try:
            user = User.objects.get(username=user)
            customer = Customer.objects.get(user=user)
            return customer
        except:
            return False
    else:
        user = request.user
        if user is not None:
            try:
                customer = Customer.objects.get(user=user)
                return customer
            except:
                return ''
        else:
            return ''


def getShipping(request, user='NoUser'):
    if user != 'NoUser':
        customer = getProfile(request, user=user)
    else:
        customer = getProfile(request)

    if customer != '':
        try:
            shipping = ShippingAddress.objects.get(customer=customer)
            return shipping
        except:
            return ''
    else:
        return ''


def checkUserEdit(request, pk):

    customer = Customer.objects.get(id=pk)
    user = customer.user

    if User.objects.filter(username=request.POST['username']).count() > 0:
        messages.info(request, 'Username Already Exists')
        return False

    if User.objects.filter(email=request.POST['email']).count() > 0:
        messages.info(request, 'Email Already Exists')
        return False

    if request.POST['email'] != '':
        try:
            validate_email(request.POST['email'])
        except:
            messages.info(request, 'Invalid Email')
            return False

    if check_password(request.POST['password'], user.password) == False:
        messages.info(request, 'Password Does not Match')
        return False

    return True


def checkProd():
    product = Product.objects.all()
    for p in product:
        if date.today() > p.valid_time.date():
            p.status = False
            try:
                p.save()
            except:
                pass

    return True


def saveInfo(request, pk):
    customer = Customer.objects.get(id=pk)
    user = customer.user
    if request.POST['username'] != '':
        user.username = request.POST['username']

    if request.POST['name'] != '':
        user.first_name = request.POST['name']
        customer.name = request.POST['name']

    if request.POST['email'] != '':
        user.email = request.POST['email']
        customer.email = request.POST['email']

    try:
        user.save()
        customer.save()
        return True
    except:
        messages.info(request, 'Something Went Wrong!')
        return False


def checkShipping(request, shipping):
    if request.POST['address'] != '':
        address = request.POST['address']
    else:
        address = shipping.address

    if request.POST['city'] != '':
        city = request.POST['city']
    else:
        city = shipping.city

    if request.POST['state'] != '':
        state = request.POST['state']
    else:
        state = shipping.state

    if request.POST['zipcode'] != '':
        zipcode = request.POST['zipcode']
    else:
        zipcode = shipping.zipcode

    return address, city, state, zipcode


def checkWishlist(request, slug):
    product = Product.objects.get(slug=slug)
    try:
        customer = Customer.objects.get(user=request.user)
    except:
        return False

    wishlist = WishList.objects.filter(customer=customer,
                                       product=product).count()
    if wishlist > 0:
        return False

    return True


def HighestBidder(prod):
    try:
        highest = Bid.objects.get(product=prod, highest=True)
        return highest
    except:
        return False


def setHighestBidder(prod, usr_amount, customer):
    if highestValueCheck(prod, usr_amount):
        bidder = HighestBidder(prod)
        if bidder != False:
            bidder.highest = False
            try:
                bidder.save()
            except:
                pass

        Bid.objects.create(customer=customer,
                           product=prod,
                           bid_amount=usr_amount,
                           highest=True)


def validBid(prod, usr_amount):
    if highestValueCheck(prod, usr_amount) and bidValueCheck(prod, usr_amount):
        return True
    else:
        return False


def highestValueCheck(prod, usr_amount):
    current = HighestBidder(prod)
    try:
        current_amt = current.bid_amount
    except:
        current_amt = prod.start_bid

    if int(usr_amount) > int(current_amt):
        return True
    else:
        return False


def bidValueCheck(prod, usr_amount):
    prod_value = prod.start_bid
    if int(usr_amount) > int(prod_value):
        return True
    else:
        return False


def biddingUser(customer, prod):
    highest = HighestBidder(prod)
    if highest == False:
        return True

    if str(highest.customer) != str(customer):
        return True
    else:
        return False


def bidAmountCheck(usr_amount, prod):
    highest = HighestBidder(prod)
    if highest:
        if int(usr_amount) <= (highest.bid_amount * 2) and int(usr_amount) >= (
                highest.bid_amount + 50):
            return True
        else:
            return False
    else:
        if int(usr_amount) <= (prod.start_bid *
                               2) and int(usr_amount) >= (prod.start_bid + 50):
            return True
        else:
            return False
