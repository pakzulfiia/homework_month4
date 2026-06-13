from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models, forms
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import F



from django.views import generic
from django.core.paginator import Paginator
from django.http import HttpResponse

class WorkerSearchView(generic.ListView):
    model = models.CustomUser
    template_name = 'workers/worker_list.html'
    context_object_name = 'worker_list'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('s', '')

        if query:
            return models.CustomUser.objects.filter(username__icontains=query).order_by('-id')
        return models.CustomUser.objects.none()

    def render_to_response(self, context, **response_kwargs):
        query = self.request.GET.get('s', '')

        if not query:
            return HttpResponse('Работник не найден!')
        return super().render_to_response(context, **response_kwargs)

# def search_view(request):
#     query = request.GET.get('s', '')

#     if query:
#         worker_list = models.CustomUser.objects.filter(username__icontains=query).order_by('-id')
#         paginator = Paginator(worker_list, 2)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)

#         return render(request,'workers/worker_list.html', {'worker_list': page_obj})
#     return HttpResponse('Работник не найден!')

class RegisterView(generic.CreateView):
    template_name = 'workers/register.html'
    model = models.CustomUser
    form_class = forms.CustomRegisterForm
    success_url = '/login/'

# def register_view(request):
#     if request.method == 'POST':
#         form = forms.CustomRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = forms.CustomRegisterForm()
#     return render(request, 
#                   template_name='workers/register.html', 
#                   context={'form': form})

class AuthLoginView(LoginView):
    template_name = 'workers/login.html'
    next_page = '/worker_list/'

    def form_valid(self, form):
        captcha = self.request.POST.get('captcha')

        if captcha == "4":
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, error="Неверная капча"))

# def auth_login_view(request):
#     error = None
#     form = AuthenticationForm(data=request.POST or None)
#     if request.method == 'POST':
#         captcha = request.POST.get('captcha')
#         if form.is_valid():
#             if captcha == "4":
#                 user = form.get_user()
#                 login(request, user)
#                 return redirect('/worker_list/')
#             else:
#                 error = "Неверная капча"
#     return render(request, 'workers/login.html', {
#         'form': form,
#         'error': error
#     })

class AuthLogoutView(LogoutView):
    next_page = '/login/'

# def auth_logut_view(request):
#     logout(request)
#     return redirect('/login/')



class WorkerListView(generic.ListView):
    model = models.CustomUser
    template_name = 'workers/worker_list.html'
    context_object_name = 'worker_list'
    paginate_by = 2

    def get_queryset(self):
        return models.CustomUser.objects.order_by('-id')

    def get(self, request, *args, **kwargs):
        view_id = request.GET.get('view')

        if view_id:
            viewed = request.session.get('viewed_worker', [])

            if int(view_id) not in viewed:
                models.CustomUser.objects.filter(id=view_id).update(views=F('views') + 1)
                viewed.append(int(view_id))
                request.session['viewed_worker'] = viewed
        return super().get(request, *args, **kwargs)


# def worker_list_view(request):
#     view_id = request.GET.get('view')

#     if view_id:
#         viewed = request.session.get('viewed_worker', [])

#         if int(view_id) not in viewed:
#             models.CustomUser.objects.filter(id=view_id).update(views=F('views')+1)
#             viewed.append(int(view_id))
#             request.session['viewed_worker'] = viewed

#     worker_list = models.CustomUser.objects.all().order_by('-id')
#     paginator = Paginator(worker_list, 2)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)

#     return render(request,'workers/worker_list.html', {'worker_list': page_obj})
