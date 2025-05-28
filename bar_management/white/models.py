from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer_statusProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    contact = models.CharField(max_length=20, blank=True, null=True)
    room_price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  
    beer_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    days_stayed = models.PositiveIntegerField(default=0)
    beers_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def compute_total_due(self):
        room_cost = self.room_price_per_day * self.days_stayed
        beer_cost = self.beer_price * self.beers_taken
        return room_cost + beer_cost

    def compute_balance(self):
        return self.compute_total_due() - self.amount_paid

class Receipt(models.Model):
    customer = models.ForeignKey(Customer_statusProfile, on_delete=models.CASCADE, related_name='receipts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt {self.id} for {self.customer.user.username} - {self.amount}"

@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        Customer_statusProfile.objects.create(user=instance)