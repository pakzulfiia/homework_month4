from django.urls import path
from . import views

urlpatterns = [
    path('create_thing/', views.create_thing_view, name='create_thing'),
    path('thing_list/', views.thing_list_view, name='thing_list',),
    path('thing_list/<int:id>/update/', views.update_thing_view, name='update_thing' ),
    path('thing_list/<int:id>/delete/', views.delete_thing_view, name='delete_thing'),
]