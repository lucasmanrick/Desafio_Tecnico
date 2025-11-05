from rest_framework import viewsets
from notification.api import serializers
from notification import models

class NotificationViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.NotificationSerializer
    queryset = models.Notification.objects.all()