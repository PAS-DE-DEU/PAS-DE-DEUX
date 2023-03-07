from django.urls import path
from . import views
from Cart.views import *

urlpatterns=[
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>/<slug:product_slug>/', views.detail, name='product-detail'),

    #Cart
    path('cart/', Cart, name='cart'),

    #Checkout
    path('checkout/', Checkout, name='checkout'),

    #Settings
    path('Orders/', views.settings, name='my-orders'),
    path('Add-address/', views.AddAddress, name='Add_address'),
]