from django.contrib import admin
from .models import Customer_statusProfile, Receipt

@admin.register(Customer_statusProfile)
class Customer_statusProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'contact', 'room_price_per_day', 'days_stayed', 'beer_price', 'beers_taken', 'amount_paid', 'compute_total_due', 'compute_balance']
    list_filter = ['days_stayed', 'beers_taken']
    search_fields = ['user__username', 'contact']

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['customer', 'amount', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['customer__user__username', 'description']