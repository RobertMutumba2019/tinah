from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def is_admin(user):
    return user.is_superuser

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('customer_status')
            else:
                messages.error(request, 'You must be an admin to access this page.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
@user_passes_test(is_admin, login_url='/login/', redirect_field_name=None)
def customer_status(request):
    # Log out the user to force re-authentication on next access/refresh
    logout(request)
    return render(request, 'customer_status.html')


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')