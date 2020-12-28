from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminIndex, name="adminIndex"),
    path('products/', views.adminProducts, name="adminProducts"),
    path('product/create/', views.createProduct, name="createProduct"),
    path('product/edit/<str:pk>', views.editProduct, name="editProduct"),
    path('product/closebid/', views.closeBid, name='closeBid'),
    path('coupons/', views.adminCoupons, name="adminCoupons"),
    path('coupon/create/', views.createCoupons, name="createCoupon"),
    path('coupon/edit/<str:pk>', views.editCoupon, name="editCoupon"),
    path('users/', views.adminUsers, name="adminUsers"),
    path('delete/user/<str:pk>', views.deleteUser, name="deleteUser"),
    path('delete/user/step/<str:pk>',
         views.deleteUserNext,
         name="deleteUserNext"),
    path('bid/change/<slug:slug>/<str:pk>',
         views.changeBidder,
         name="changeBidder"),
    path('delete/product/<str:pk>', views.deleteProd, name="deleteProd"),
    path('delete/coupon/<str:pk>', views.deleteCoup, name="deleteCoup"),
    path('shipping/<str:pk>', views.shippingAccess, name="shippingAccess"),
    path('prod/activate/<slug:slug>', views.activateProd, name="activateProd"),
]