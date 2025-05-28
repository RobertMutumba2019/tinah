from django import forms
from django.contrib.auth.models import User
from .models import Customer_statusProfile, Receipt

class ClientForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    contact = forms.CharField(max_length=20, required=False)
    amount_paid = forms.DecimalField(max_digits=10, decimal_places=2, initial=0.00)
    room_price_per_day = forms.DecimalField(max_digits=10, decimal_places=2, initial=0.00)
    beer_price = forms.DecimalField(max_digits=10, decimal_places=2, initial=0.00)
    days_stayed = forms.IntegerField(initial=0)
    beers_taken = forms.IntegerField(initial=0)

    class Meta:
        model = Customer_statusProfile
        fields = ['amount_paid', 'contact', 'room_price_per_day', 'beer_price', 'days_stayed', 'beers_taken']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        profile = super().save(commit=False)
        profile.user = user
        if commit:
            profile.save()
        return profile

class ReceiptForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer_statusProfile.objects.all())

    class Meta:
        model = Receipt
        fields = ['customer', 'amount', 'description']