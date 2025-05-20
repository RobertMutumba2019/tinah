
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def customer_status(request):
    return render(request, 'customer_status.html')
