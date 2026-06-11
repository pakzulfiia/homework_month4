from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.core.paginator import Paginator
from django.db.models import F



def search_view(request):
    query = request.GET.get('s', '')
    if query:
        book = models.Books.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден!')
    
    return render(request, template_name='books_smth/books_list.html',
                  context={'book': book})


def books_list_view(request):
    if request.method == 'GET':
        book = models.Books.objects.all().order_by("-id")
        paginator = Paginator(book, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        context = {
            'book': page_obj,
        }
        return render(request, template_name='books_smth/books_list.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)

        views_blog = request.session.get('viewed_blog', [])
        if id not in views_blog:
            book_id.views = F('views')+1
            book_id.save()
            book_id.refresh_from_db()
        views_blog.append(id)
        request.session['viewed_blog'] = views_blog


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