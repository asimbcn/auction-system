from django.shortcuts import render, redirect
from .models import *
from Customer.models import *
from django.contrib.auth.decorators import login_required
from Customer.utils import *
from .forms import CreateProduct, CreateCoupon
from django.http import JsonResponse
from datetime import datetime, timedelta
import json


# Create your views here.
@login_required(login_url='login')
def adminIndex(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    context = {'index': 'true'}
    return render(request, 'adminpanel/index.html', context)


@login_required(login_url='login')
def adminProducts(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    data = getProduct(request)
    context = {'products': 'true', 'allProd': data['allProd']}

    return render(request, 'adminpanel/product.html', context)


@login_required(login_url='login')
def createProduct(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    error = ''
    form = CreateProduct()

    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminProducts')
        else:
            error = 'Product Creation Failed!'

    context = {'products': 'true', 'form': form, 'error': error}

    return render(request, 'adminpanel/create_product.html', context)


@login_required(login_url='login')
def editProduct(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    prod = Product.objects.get(id=pk)
    error = ''
    form = CreateProduct(instance=prod)

    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('adminProducts')
        else:
            error = 'Product Update Failed!'

    context = {'products': 'true', 'form': form, 'error': error}

    return render(request, 'adminpanel/update_product.html', context)


@login_required(login_url='login')
def activateProd(request, slug):
    if check_permission(request)['status'] == False:
        return redirect('home')

    product = Product.objects.get(slug=slug)

    if product.status:
        product.status = False
    else:
        product.valid_time = datetime.now() + timedelta(days=7)
        product.status = True

    deleteCart(request, slug)
    try:
        product.save()
        return redirect('adminProducts')
    except:
        pass


def closeBid(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        slugData = data['slug']
        product = Product.objects.get(slug=slugData)
        product.status = False
        cartCheck(request, product.slug)
        try:
            product.save()
            return JsonResponse('Product Expired', safe=False)
        except:
            pass


@login_required(login_url='login')
def adminCoupons(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    data = getCoupon(request)
    context = {'coupons': 'true', 'allCoup': data['allCoup']}

    return render(request, 'adminpanel/coupons.html', context)


@login_required(login_url='login')
def createCoupons(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    error = ''
    form = CreateCoupon()

    if request.method == 'POST':
        form = CreateCoupon(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminCoupons')
        else:
            error = 'Coupon Creation Failed!'

    context = {'coupons': 'true', 'form': form, 'error': error}

    return render(request, 'adminpanel/create_coupon.html', context)


@login_required(login_url='login')
def editCoupon(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    coup = Coupon.objects.get(id=pk)
    error = ''
    form = CreateCoupon(instance=coup)

    if request.method == 'POST':
        form = CreateCoupon(request.POST, instance=coup)
        if form.is_valid():
            form.save()
            return redirect('adminCoupons')
        else:
            error = 'Coupon Creation Failed!'

    context = {'coupons': 'true', 'form': form, 'error': error}

    return render(request, 'adminpanel/update_coupon.html', context)


@login_required(login_url='login')
def adminUsers(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    users = User.objects.all()
    shipping = ShippingAddress.objects.all()

    context = {'users': 'true', 'data': users, 'shipping': shipping}
    return render(request, 'adminpanel/users.html', context)


@login_required(login_url='login')
def deleteUser(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    user = User.objects.get(id=pk)
    highest = Bid.objects.filter(customer=user.customer, highest=True).count()

    if highest > 0:
        return redirect(deleteUserNext, pk=pk)
    return redirect('adminUsers')


@login_required(login_url='login')
def deleteUserNext(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    user = User.objects.get(id=pk)
    highest = Bid.objects.filter(customer=user.customer, highest=True)
    context = {'users': 'true', 'data': highest, 'user': user}
    return render(request, 'adminpanel/specificUser.html', context)


@login_required(login_url='login')
def changeBidder(request, slug, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    user = User.objects.get(id=pk)
    product = Product.objects.get(slug=slug)
    current = Bid.objects.get(customer=user.customer,
                              product=product,
                              highest=True)
    new = Bid.objects.filter(product=product, highest=False).last()
    if current:
        user.delete()

    new.highest = True
    try:
        new.save()
    except:
        pass

    return redirect('adminUsers')


@login_required(login_url='login')
def shippingAccess(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    customer = Customer.objects.get(id=pk)
    shipping = ShippingAddress.objects.get(customer=customer)

    if shipping.edit != True:
        shipping.edit = True
        try:
            shipping.save()
        except:
            pass

    return redirect('adminUsers')


@login_required(login_url='login')
def deleteProd(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    prod = Product.objects.get(id=pk)
    prod.delete()
    return redirect('adminProducts')


@login_required(login_url='login')
def deleteCoup(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    Coup = Coupon.objects.get(id=pk)
    Coup.delete()
    return redirect('adminCoupons')
