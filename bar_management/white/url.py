from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

 

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('customer_status/', views.customer_status, name='customer_status'),
    path('login/', views.custom_login, name='login'),
]
