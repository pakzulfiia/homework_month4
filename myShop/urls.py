from django.urls import path
from . import views

urlpatterns =[
    path('categories/', views.categories_view, name='categories'),
    path('products/', views.products_view, name='products'),
    path('categories/<int:id>/', views.category_products_view, name='category_products'),
]