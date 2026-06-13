from django.urls import path
from . import views


urlpatterns = [
    path('books_info/', views.BooksInfoView.as_view(), name='books_info'),
    path('books_list/', views.BooksListView.as_view(), name='books_list'),
    path('books_list/<int:id>/', views.BookDetailView.as_view(), name='book_id'),
    path('search/', views.SearchView.as_view(), name='search'),

]
