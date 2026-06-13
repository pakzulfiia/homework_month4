from django.urls import path
from . import views

urlpatterns = [
    path('horse_tour/', views.HorseTourListView.as_view(), name='horse_list'),
    path('tour_search/', views.SearchView.as_view(), name='tour_search'),
]