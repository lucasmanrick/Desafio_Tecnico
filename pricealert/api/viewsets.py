from rest_framework import viewsets
from pricealert.api import serializers
from pricealert import models

class PriceAlertViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.PriceAlertSerializer
    queryset = models.PriceAlert.objects.all()