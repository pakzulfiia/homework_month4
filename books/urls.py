from django.urls import path
from . import views


urlpatterns = [
    path('books_info/', views.books_info_view, name='books_info'),
    path('books_list/', views.books_list_view, name='books_list'),
    path('books_list/<int:id>/', views.book_detail_view, name='book_id'),
]
