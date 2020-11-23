from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    start_bid = models.IntegerField(null=True, blank=True)
    max_bid = models.IntegerField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    status = models.BooleanField(default=True, null=True, blank=False)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    valid_time = models.DateTimeField(blank=True, null=True)
    seller = models.CharField(max_length=200, null=True)
    condition = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title