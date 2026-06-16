from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models, forms
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.



class RegisterView(generic.CreateView):
    template_name = 'movies/register.html'
    model = User
    form_class = forms.RegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(RegisterView, self).form_valid(form=form)
    

class AuthLoginView(LoginView):
    template_name = 'movies/login.html'
    next_page = '/movie_list/'


class AuthLogoutView(LogoutView):
    next_page = '/login/'
    

class MovieListView(generic.ListView):
    model = models.Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 2

    def get_queryset(self):
        queryset = models.Movie.objects.all()
        search = self.request.GET.get('s')
        if search:
            queryset = queryset.filter(title__icontains=search)

        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genres__id=genre)

        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = models.Genre.objects.all()
        return context
        

class MovieDetailView(generic.DetailView):
    model = models.Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-id')
        context['comment_form'] = forms.CommentForm()
        return context
    
@login_required
def add_comment(request, pk):
    movie = get_object_or_404(models.Movie, pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author = request.user
            comment.save()
    return redirect('movie_detail', pk=pk)

class CreateMovieView(generic.CreateView):
    model = models.Movie
    form_class = forms.MovieForm
    template_name = 'movies/create_movie.html'
    success_url = '/movie_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateMovieView, self).form_valid(form=form)
    
class UpdateMovieView(generic.UpdateView):
    model = models.Movie
    form_class = forms.MovieForm
    template_name = 'movies/update_movie.html'
    success_url = '/movie_list/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=movie_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateMovieView, self).form_valid(form=form)
    

class DeleteMovieView(generic.DeleteView):
    model = models.Movie
    template_name = 'movies/confirm_delete.html'
    success_url = '/movie_list/'
    context_object_name = 'movie_id'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=movie_id)
    

@login_required
def reserved_vip(request, pk):
    movie = get_object_or_404(models.Movie, pk=pk)
    if models.Vip.objects.filter(user=request.user).exists():
        messages.info(request, "У вас уже есть VIP место")
        return redirect('movie_detail', pk=pk)
    taken = models.Vip.objects.values_list('seat_num', flat=True)
    seat_num = 1
    while seat_num in taken:
        seat_num += 1
    vip = models.Vip.objects.create(user=request.user, movie=movie, seat_num=seat_num)
    messages.success(request, f"VIP место успешно забронировано: {seat_num}")
    return redirect('movie_detail', pk=pk)
