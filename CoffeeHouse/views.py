from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Products, CategoriesOfProducts

def root(request):
    return render(request, 'main-catalog.html')

def catalog(request):
    # получаем все продукты
    products = Products.objects.all().order_by('name')
    
    # получаем все категории
    all_categories = CategoriesOfProducts.objects.all().order_by('category_name')
    
    # проверяем, есть ли параметр 'category' в GET запросе
    selected_category_id = request.GET.get('category')
    
    # если параметр 'category' существует и это не пустая строка
    if selected_category_id:
        # получаем категорию по ID
        try:
            selected_category = CategoriesOfProducts.objects.get(id=selected_category_id)
            products = products.filter(category=selected_category) # фильтруем продукты по выбранной категории
        except CategoriesOfProducts.DoesNotExist:
            # если категория не найдена, ничего не фильтруем 
            pass

    # --- код для поиска аааа ---
    # получаем параметр 'search' из GET запроса
    search_query = request.GET.get('search')
    
    # если параметр 'search' существует и не пустой
    if search_query:
        # фильтруем продукты по названию, игнорируя регистр
        products = products.filter(name__icontains=search_query)

    return render(request, 'catalog.html', {
        'products': products,
        'categories': all_categories,
        'selected_category_id': int(selected_category_id) if selected_category_id else None,
        'search_query': search_query,
    })

def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product-detail.html', {'product': product})