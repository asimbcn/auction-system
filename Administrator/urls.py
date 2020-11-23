from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminIndex, name="adminIndex"),
    path('products/', views.adminProducts, name="adminProducts"),
    path('product/create/', views.createProduct, name="createProduct"),
    path('coupons/', views.adminCoupons, name="adminCoupons"),
    path('users/', views.adminUsers, name="adminUsers"),
    path('delete/user/<str:pk>', views.deleteUser, name="deleteUser"),
    path('delete/product/<str:pk>', views.deleteProd, name="deleteProd"),
]