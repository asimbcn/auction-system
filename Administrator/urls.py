from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminIndex, name="adminIndex"),
    path('products/', views.adminProducts, name="adminProducts"),
    path('coupons/', views.adminCoupons, name="adminCoupons"),
    path('users/', views.adminUsers, name="adminUsers"),
]