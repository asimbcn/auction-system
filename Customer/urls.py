from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('cart/', views.cart, name="cart"),
    path('coupons/', views.coupons, name="coupons")
]