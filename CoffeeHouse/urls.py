from django.urls import path
from .views import root, catalog, product_detail
from django.shortcuts import render

urlpatterns = [
    path('', root, name='main-catalog'),
    path('catalog/', catalog, name='catalog'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]