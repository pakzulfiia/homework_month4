from django.urls import path
from . import views

urlpatterns = [
    path('create_thing/', views.CreateThingView.as_view(), name='create_thing'),
    path('thing_list/', views.ThingListView.as_view(), name='thing_list',),
    path('thing_list/<int:id>/update/', views.UpdateThingView.as_view(), name='update_thing' ),
    path('thing_list/<int:id>/delete/', views.DeleteThingView.as_view(), name='delete_thing'),
]