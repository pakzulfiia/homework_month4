from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models



def books_list_view(request):
    if request.method == 'GET':
        book = models.Books.objects.all().order_by("-id")
        context = {
            'book': book,
        }
        return render(request, template_name='books_smth/books_list.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {
            'book_id': book_id
        }
        return render(request, template_name='books_smth/book_detail.html', context=context)
    

def books_info_view(request):
    if request.method == 'GET':
        context = {
            'title': '1984',
            'author': 'Джордж Оруэлл',
            'publication_year': 1949,
            'sells': '22 000 экземпляров книги'
        }
    return render(request, 'books_info.html', context)