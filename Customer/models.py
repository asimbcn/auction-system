from django.db import models
from django.contrib.auth.models import User
from Administrator.models import Product, Coupon
from datetime import datetime

CURRENT_DATE = datetime.now()


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    image = models.ImageField(upload_to="profile/", null=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/media/placeholder.png'

        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.customer}'s Order"

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product}"

    @property
    def get_total(self):
        total = self.product.start_bid * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    edit = models.BooleanField(default=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"


class WishList(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    def __str__(self):
        return f"{self.customer}'s Wish"


class Bid(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    bid_amount = models.IntegerField(default=0, null=True, blank=True)
    highest = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=CURRENT_DATE, null=True)

    def __str__(self):
        return f"{self.customer}'s Bid for {self.product}"
