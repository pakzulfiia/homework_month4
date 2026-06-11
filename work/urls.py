from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='reg'),
    path('login/', views.auth_login_view, name='log'),
    path('logout/', views.auth_logut_view, name='unlog'),
    path('worker_list/', views.worker_list_view, name='worker_list'),
    path('search/', views.search_view, name='search'),

]