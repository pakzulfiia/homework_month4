from django.urls import path
from . import views


urlpatterns = [
    path('books_info/', views.books_info_view, name='books_info'),
]
