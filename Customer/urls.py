from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('adminSelect', views.adminSelect, name="adminSelect"),
    path('register/', views.register, name="register"),
    path('cart/', views.cart, name="cart"),
    path('view/<slug:slug>', views.viewProduct, name="view"),
    path('product/<slug:slug>', views.completeProduct, name="completeProduct"),
    path('edit/photo/<str:pk>', views.editPhoto, name="editPhoto"),
    path('edit/user/<str:pk>', views.editUser, name="editUser"),
    path('edit/shipping/<str:pk>', views.editShipping, name="editShipping"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('profile/<str:user>/', views.Userprofile, name="profile"),
]