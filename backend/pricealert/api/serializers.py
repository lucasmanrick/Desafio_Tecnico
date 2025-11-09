from rest_framework import serializers
from pricealert import models


class PriceAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PriceAlert
        fields = '__all__'