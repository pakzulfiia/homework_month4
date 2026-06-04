from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
# Create your views here.

def create_thing_view(request):
    if request.method == 'POST':
        form = forms.ThingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/thing_list/')
    else:
        form = forms.ThingForm()
    context = {
        'form': form
    }
    return render(request, template_name='crud/create_thing.html', context=context)

def thing_list_view(request):
    if request.method == 'GET':
        thing = models.Thing.objects.all().order_by('-id')
        context = {
            'thing': thing
        }
        return render(request, template_name='crud/thing_list.html', context=context)

def update_thing_view(request, id):
    thing_id = get_object_or_404(models.Thing, id=id)
    if request.method == 'POST':
        form = forms.ThingForm(request.POST, instance=thing_id)
        if form.is_valid():
            form.save()
            return redirect('/thing_list/')
    else:
        form = forms.ThingForm(instance=thing_id)
    context = {
            'form': form,
            'thing_id': thing_id
    }
    return render(request, template_name='crud/update_thing.html', context=context)

def delete_thing_view(request, id):
    thing_id = get_object_or_404(models.Thing, id=id)
    thing_id.delete()
    return redirect('/thing_list/')