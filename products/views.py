from django.shortcuts import render, get_object_or_404  # Импорт функции get_object_or_404
from products.models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products_detail.html', {'product': product})

