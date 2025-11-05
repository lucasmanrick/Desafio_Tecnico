from django.db import models
from uuid import uuid4
from user.models import User

# Create your models here.



class PortfolioHolding(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holdings')
    coin_id = models.CharField(max_length=100)
    coin_name = models.CharField(max_length=255)
    coin_symbol = models.CharField(max_length=20)
    coin_image = models.URLField()
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    purchase_price_usd = models.DecimalField(max_digits=20, decimal_places=2)
    purchase_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
