from django.urls import path
from . import views

urlpatterns = [
    path('horse_tour/', views.horse_tour_list_view, name='horse_list')
]