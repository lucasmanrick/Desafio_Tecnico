from rest_framework import viewsets
from notification.api import serializers
from notification import models

class NotificationViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.NotificationSerializer



    def get_queryset(self):
        # retorna apenas notificações do usuário logado
        return self.queryset.filter(user=self.request.user)