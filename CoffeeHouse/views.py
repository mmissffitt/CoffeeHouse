from django.shortcuts import render, HttpResponse 

def root(request):
    return render(request, 'main-catalog.html')