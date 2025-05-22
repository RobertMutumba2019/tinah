
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def customer_status(request):
    if not request.user.is_authenticated:  # Check if the user is logged in
        return redirect('index')  # Redirect to the index page if not authenticated
    return render(request, 'customer_status.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')  # Ensure index.html exists

def Bar(request):
    return render(request, 'Bar.html')

def Garden(request):
    return render(request, 'Garden.html')

def product(request):
    return render(request, 'product.html')