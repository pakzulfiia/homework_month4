from django.urls import path
from . import views

urlpatterns =[
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('products/', views.ProductView.as_view(), name='products'),
    path('categories/<int:id>/', views.CategoryProductsView.as_view(), name='category_products'),
]