from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Customer_statusProfile, Receipt
from .forms import ClientForm, ReceiptForm

@staff_member_required
def customer_status(request):
    
    profiles = Customer_statusProfile.objects.all()
    # Some logic accessing profile.room_price_per_day
    return render(request, 'customer_status.html', {'profiles': profiles})
    if request.method == 'POST':
        if 'add_client' in request.POST:
            client_form = ClientForm(request.POST)
            if client_form.is_valid():
                client_form.save()
                return redirect('customer_status')
        elif 'add_receipt' in request.POST:
            receipt_form = ReceiptForm(request.POST)
            if receipt_form.is_valid():
                receipt_form.save()
                return redirect('customer_status')
        elif 'delete_client' in request.POST:
            client_id = request.POST.get('client_id')
            client = get_object_or_404(Customer_statusProfile, id=client_id)
            client.user.delete()
            return redirect('customer_status')
    else:
        client_form = ClientForm()
        receipt_form = ReceiptForm()
    
    clients = Customer_statusProfile.objects.all()
    return render(request, 'customer_status.html', {
        'clients': clients,
        'client_form': client_form,
        'receipt_form': receipt_form
    })

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')