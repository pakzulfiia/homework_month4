from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
# Create your views here.
# Реализуйте функцию (view), которая возвращает все продукты, относящиеся к выбранной категории.
# Реализуйте функцию, которая возвращает список всех категорий.


class ProductView(generic.TemplateView):
    template_name = 'myShop/products.html'
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = models.Product.objects.all()
        return context

# def products_view(request):
#     if request.method == 'GET':
#         products = models.Product.objects.all()
#         context = {
#             'products': products
#         }
#         return render(request,template_name='myShop/products.html',context=context)
    
class CategoryProductsView(generic.TemplateView):
    template_name = 'myShop/category_products.html'
    model = models.Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = models.Category.objects.all()
        context['products'] = models.Product.objects.all()
        return context



# def category_products_view(request, id):
#     if request.method == 'GET':
#         category = get_object_or_404(models.Category, id=id)
#         products = category.products.all()
#         context = {
#             'category': category,
#             'products': products
#         }
#         return render(request, template_name='myShop/category_products.html', context=context)
    

class CategoriesView(generic.TemplateView):
    template_name = 'myShop/categories.html'
    model = models.Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context


# def categories_view(request):
#     if request.method == 'GET':
#         categories = models.Category.objects.all()
#         context = {
#             'categories': categories
#         }
#         return render(request, template_name='myShop/categories.html', context=context)