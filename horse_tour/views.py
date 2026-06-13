from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic



class SearchView(generic.ListView):
    template_name = 'horse_tour.html'
    context_object_name = 'tours'
    model = models.HorseTour
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
    
# def search_view(request):
#     query = request.GET.get('s', '')

#     if query:
#         tours = models.HorseTour.objects.filter(title__icontains=query).order_by('-id')
#         paginator = Paginator(tours, 2)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)

#         return render(request, 'horse_tour.html', {'tours': page_obj,})
#     return HttpResponse('Тур не найден!')


class HorseTourListView(generic.ListView):
    template_name = 'horse_tour.html'
    model = models.HorseTour
    context_object_name = 'tours'
    paginate_by = 2

    def get_queryset(self):
        return models.HorseTour.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['horses'] = models.ChoiceHorse.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        view_id = request.GET.get('view')

        if view_id:
            viewed = request.session.get('viewed_tour', [])

            if int(view_id) not in viewed:
                models.HorseTour.objects.filter(id=view_id).update(views=F('views') + 1)

                viewed.append(int(view_id))
                request.session['viewed_tour'] = viewed

        return super().get(request, *args, **kwargs)


# def horse_tour_list_view(request):
#     view_id = request.GET.get('view')

#     if view_id:
#         viewed = request.session.get('viewed_tour', [])

#         if int(view_id) not in viewed:
#             models.HorseTour.objects.filter(id=view_id).update(views=F('views')+1)
#             viewed.append(int(view_id))
#             request.session['viewed_tour'] = viewed

#     tours = models.HorseTour.objects.all().order_by('-id')
#     paginator = Paginator(tours, 2)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)
#     horses = models.ChoiceHorse.objects.all()

#     return render(request, 'horse_tour.html', {'tours': page_obj, 'horses': horses, })


