from django.shortcuts import render, redirect
from .models import *
from Customer.models import *
from django.contrib.auth.decorators import login_required
from Customer.utils import check_permission


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

    context = {'products': 'true'}
    return render(request, 'adminpanel/product.html', context)


@login_required(login_url='login')
def adminCoupons(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    context = {'coupons': 'true'}
    return render(request, 'adminpanel/coupons.html', context)


@login_required(login_url='login')
def adminUsers(request):
    if check_permission(request)['status'] == False:
        return redirect('home')

    users = User.objects.all()

    context = {'users': 'true', 'data': users}
    return render(request, 'adminpanel/users.html', context)