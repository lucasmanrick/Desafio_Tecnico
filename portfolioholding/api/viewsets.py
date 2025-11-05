from rest_framework import viewsets
from portfolioholding.api import serializers
from portfolioholding import models

class PortfolioHoldingViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.PortfolioHoldingSerializer
    queryset = models.PortfolioHolding.objects.all()