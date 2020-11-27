from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

CURRENT_DATE = datetime.now()
VALID = datetime.now() + timedelta(days=7)


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    start_bid = models.IntegerField(null=True)
    max_bid = models.IntegerField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to="products/", null=True)
    status = models.BooleanField(default=True, null=True, blank=False)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=CURRENT_DATE, null=True)
    valid_time = models.DateTimeField(default=VALID, null=True)
    seller = models.CharField(max_length=200, null=True)
    condition = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title