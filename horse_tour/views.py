from django.shortcuts import render
from . import models
# Create your views here.
def horse_tour_list_view(request):
    if request.method == 'GET':
        tour = models.HorseTour.objects.all()
        horse = models.ChoiceHorse.objects.all()
        context = {
            'tours': tour,
            'horses': horse,
        }
        return render(request, template_name='horse_tour.html', context=context)