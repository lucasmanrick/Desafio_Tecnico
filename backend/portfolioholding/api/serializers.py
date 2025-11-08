from rest_framework import serializers
from portfolioholding import models


class PortfolioHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PortfolioHolding
        fields = '__all__'