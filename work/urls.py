from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='reg'),
    path('login/', views.AuthLoginView.as_view(), name='log'),
    path('logout/', views.AuthLogoutView.as_view(), name='unlog'),
    path('worker_list/', views.WorkerListView.as_view(), name='worker_list'),
    path('worker_search/',  views.WorkerSearchView.as_view(), name='worker_search'),

]