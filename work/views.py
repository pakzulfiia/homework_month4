from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models, forms

def register_view(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()
    return render(request, 
                  template_name='workers/register.html', 
                  context={'form': form})


def auth_login_view(request):
    error = None
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        captcha = request.POST.get('captcha')
        if form.is_valid():
            if captcha == "4":
                user = form.get_user()
                login(request, user)
                return redirect('/worker_list/')
            else:
                error = "Неверная капча"
    return render(request, 'workers/login.html', {
        'form': form,
        'error': error
    })

def auth_logut_view(request):
    logout(request)
    return redirect('/login/')


def worker_list_view(request):
    if request.method == 'GET':
        worker_list = models.CustomUser.objects.all().order_by('-id')
    return render(request, 'workers/worker_list.html', {'worker_list': worker_list})


