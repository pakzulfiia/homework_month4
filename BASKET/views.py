from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
# Create your views here.


class CreateThingView(generic.CreateView):
    template_name = 'crud/create_thing.html'
    form_class = forms.ThingForm
    model = models.Thing
    success_url = '/thing_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateThingView, self).form_valid(form=form)



# def create_thing_view(request):
#     if request.method == 'POST':
#         form = forms.ThingForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/thing_list/')
#     else:
#         form = forms.ThingForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name='crud/create_thing.html', context=context)


class ThingListView(generic.ListView):
    template_name = 'crud/thing_list.html'
    model = models.Thing
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['thing'] = models.Thing.objects.all().order_by('-id')
        return context

# def thing_list_view(request):
#     if request.method == 'GET':
#         thing = models.Thing.objects.all().order_by('-id')
#         context = {
#             'thing': thing
#         }
#         return render(request, template_name='crud/thing_list.html', context=context)

class UpdateThingView(generic.UpdateView):
    template_name = 'crud/update_thing.html'
    form_class = forms.ThingForm
    success_url = '/thing_list/'
    model = models.Thing

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=game_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateThingView, self).form_valid(form=form)


# def update_thing_view(request, id):
#     thing_id = get_object_or_404(models.Thing, id=id)
#     if request.method == 'POST':
#         form = forms.ThingForm(request.POST, instance=thing_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/thing_list/')
#     else:
#         form = forms.ThingForm(instance=thing_id)
#     context = {
#             'form': form,
#             'thing_id': thing_id
#     }
#     return render(request, template_name='crud/update_thing.html', context=context)


class DeleteThingView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/thing_list/'
    context_object_name = 'thing_id'
    model = models.Thing

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=game_id)
    
# def delete_thing_view(request, id):
#     thing_id = get_object_or_404(models.Thing, id=id)
#     thing_id.delete()
#     return redirect('/thing_list/')