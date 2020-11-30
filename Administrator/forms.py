from django.forms import ModelForm
from django import forms
from .models import *


class CreateProduct(ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['status', 'date_created', 'valid_time']


class CreateCoupon(ModelForm):
    class Meta:
        model = Coupon
        # fields = '__all__'
        exclude = ['active']
