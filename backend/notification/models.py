from django.db import models
from uuid import uuid4
from user.models import User

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=50) # price_alert, portfolio_update, etc
    title = models.CharField(max_length=255)
    message = models.TextField()
    data = models.JSONField(default=dict) # dados adicionais
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']    