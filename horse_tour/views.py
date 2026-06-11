from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F


def search_view(request):
    query = request.GET.get('s', '')

    if query:
        tours = models.HorseTour.objects.filter(title__icontains=query).order_by('-id')
        paginator = Paginator(tours, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        return render(request, 'horse_tour.html', {'tours': page_obj,})
    return HttpResponse('Тур не найден!')


def horse_tour_list_view(request):
    view_id = request.GET.get('view')

    if view_id:
        viewed = request.session.get('viewed_tour', [])

        if int(view_id) not in viewed:
            models.HorseTour.objects.filter(id=view_id).update(views=F('views')+1)
            viewed.append(int(view_id))
            request.session['viewed_tour'] = viewed

    tours = models.HorseTour.objects.all().order_by('-id')
    paginator = Paginator(tours, 2)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    horses = models.ChoiceHorse.objects.all()

    return render(request, 'horse_tour.html', {'tours': page_obj, 'horses': horses, })


