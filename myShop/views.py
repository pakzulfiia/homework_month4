from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
# Реализуйте функцию (view), которая возвращает все продукты, относящиеся к выбранной категории.
# Реализуйте функцию, которая возвращает список всех категорий.

def products_view(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        context = {
            'products': products
        }
        return render(request,template_name='myShop/products.html',context=context)
    
def category_products_view(request, id):
    if request.method == 'GET':
        category = get_object_or_404(models.Category, id=id)
        products = category.products.all()
        context = {
            'category': category,
            'products': products
        }
        return render(request, template_name='myShop/category_products.html', context=context)
    
    
def categories_view(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, template_name='myShop/categories.html', context=context)