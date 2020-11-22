from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name