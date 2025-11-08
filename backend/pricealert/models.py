from django.db import models
from user.models import User
from uuid import uuid4

# Create your models here.
class PriceAlert(models.Model):
    CONDITION_CHOICES = [
    ('above', 'Above'),
    ('below', 'Below'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    coin_id = models.CharField(max_length=100)
    coin_name = models.CharField(max_length=255)
    coin_symbol = models.CharField(max_length=20)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    target_price_usd = models.DecimalField(max_digits=20, decimal_places=2)
    is_active = models.BooleanField(default=True)
    triggered = models.BooleanField(default=False)
    triggered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']