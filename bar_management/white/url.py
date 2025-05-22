from django.urls import path
from . import views
 

urlpatterns = [
  


    path('', views.index, name='index'),  # Ensure index is set as the default route
    path('customer_status/', views.customer_status, name='customer_status'),
    path('contact/', views.contact, name='contact'),
    path('Bar/', views.Bar, name='Bar'),
    path('Garden/', views.Garden, name='Garden'),
    path('product/', views.product, name='product'),
]
