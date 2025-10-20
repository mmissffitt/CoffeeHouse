from django.urls import path
from .views import root
from django.shortcuts import render

def main_view(request):
    return render(request, 'main-catalog.html')

urlpatterns = [
    path('', root, name='index'),
]