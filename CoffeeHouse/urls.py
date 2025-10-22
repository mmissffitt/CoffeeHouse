from django.urls import path
from .views import root
from django.shortcuts import render

urlpatterns = [
    path('', root, name='main-catalog'),
]