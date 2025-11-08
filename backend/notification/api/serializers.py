from rest_framework import serializers
from rest_framework import serializers
from notification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'type', 'title', 'message', 'data', 'read', 'created_at']
        read_only_fields = ['id', 'created_at']