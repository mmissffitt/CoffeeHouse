from django.urls import path
from .views import root, catalog
from django.shortcuts import render

urlpatterns = [
    path('', root, name='main-catalog'),
    path('catalog/', catalog, name='catalog'),
]