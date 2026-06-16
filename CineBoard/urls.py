from django.urls import path
from . import views

urlpatterns = [
    path('register_movie/', views.RegisterView.as_view(), name='register_movie'),
    path('login_movie/', views.AuthLoginView.as_view(), name='login_movie'),
    path('logout_movie/', views.AuthLogoutView.as_view(), name='unlogin'),
    path('create_movie/', views.CreateMovieView.as_view(), name='create_movie'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_list/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie_list/<int:pk>/comment/',views.add_comment, name='add_comment'),
    path('movie_list/<int:pk>/vip/',views.reserved_vip,name='reserved_vip'),
    path('movie_list/<int:id>/update/', views.UpdateMovieView.as_view(), name='update_movie'),
    path('movie_list/<int:id>/delete/', views.DeleteMovieView.as_view(), name='del_movie'),
]
