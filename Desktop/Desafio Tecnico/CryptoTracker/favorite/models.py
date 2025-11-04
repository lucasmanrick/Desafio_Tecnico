from django.db import models
from uuid import uuid4
from user.models import User

# Create your models here.
class Favorite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    coin_id = models.CharField(max_length=100) # ID do CoinGecko
    coin_name = models.CharField(max_length=255)
    coin_symbol = models.CharField(max_length=20)
    coin_image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'coin_id')
        ordering = ['-created_at']