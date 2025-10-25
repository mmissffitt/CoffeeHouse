from django.shortcuts import render, HttpResponse 
from .models import Products, CategoriesOfProducts 

def root(request):
    return render(request, 'main-catalog.html')

def catalog(request):
    # Получаем все продукты
    products = Products.objects.all().order_by('name')
    
    # Получаем все категории
    all_categories = CategoriesOfProducts.objects.all().order_by('category_name')
    
    # Проверяем, есть ли параметр 'category' в GET-запросе
    selected_category_id = request.GET.get('category')
    
    # Если параметр 'category' существует и это не пустая строка
    if selected_category_id:
        # Пытаемся получить категорию по ID
        try:
            selected_category = CategoriesOfProducts.objects.get(id=selected_category_id)
            products = products.filter(category=selected_category) # Фильтруем продукты по выбранной категории
        except CategoriesOfProducts.DoesNotExist:
            # Если категория не найдена, ничего не фильтруем (или можно показать сообщение об ошибке)
            pass
            
    # Добавляем класс 'active' к текущему выбранному фильтру
    # Это можно сделать, передав ID выбранной категории в шаблон
    
    return render(request, 'catalog.html', {
        'products': products,
        'categories': all_categories,
        'selected_category_id': int(selected_category_id) if selected_category_id else None, # Передаем ID выбранной категории для подсветки
    })