from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('cart/', views.cart, name="cart"),
    path('products/', views.products, name="products"),
    path('coupons/', views.coupons, name="coupons"),
    path('contact/', views.contact, name="contact"),
]