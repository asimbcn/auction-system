from django.shortcuts import render, redirect
from .models import *
from Customer.models import *
from django.contrib.auth.decorators import login_required
from Customer.utils import check_permission, getProduct
from .forms import CreateProduct


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


@login_required(login_url='login')
def deleteUser(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    user = User.objects.get(id=pk)
    user.delete()
    return redirect('adminUsers')


@login_required(login_url='login')
def deleteProd(request, pk):
    if check_permission(request)['status'] == False:
        return redirect('home')

    prod = Product.objects.get(id=pk)
    prod.delete()
    return redirect('adminProducts')
