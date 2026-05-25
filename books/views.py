from django.shortcuts import render
from django.http import HttpResponse

def books_info_view(request):
    if request.method == 'GET':
        context = {
            'title': '1984',
            'author': 'Джордж Оруэлл',
            'publication_year': 1949,
            'sells': '22 000 экземпляров книги'
        }
    return render(request, 'books_info.html', context)