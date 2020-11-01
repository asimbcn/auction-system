from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    context = {}
    return render(request, 'customer/index.html', context)
