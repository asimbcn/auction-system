from django.forms import ModelForm
from django import forms
from .models import *


class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'