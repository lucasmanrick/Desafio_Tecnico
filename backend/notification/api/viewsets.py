from rest_framework import viewsets
from notification.api import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from notification.models import Notification
from notification.api.serializers import NotificationSerializer



class NotificationViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.NotificationSerializer



    def get_queryset(self):
        # retorna apenas notificações do usuário logado
        return self.queryset.filter(user=self.request.user)
    

    @action(detail=True, methods=['patch'], url_path='read')
    def mark_as_read(self, request, pk=None):
        """
        PATCH /api/notifications/{id}/read/
        Marca a notificação como lida e retorna apenas id e read.
        """
        notification = self.get_object() 

        if not notification.read:
            notification.read = True
            notification.save(update_fields=['read'])

        return Response({
            "id": str(notification.id),
            "read": notification.read
        }, status=status.HTTP_200_OK)