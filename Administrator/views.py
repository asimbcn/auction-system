from django.shortcuts import render, redirect
from .models import *
from Customer.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def adminIndex(request):
    context = {}
    return render(request, 'admin/index.html', context)
