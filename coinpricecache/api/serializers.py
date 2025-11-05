from rest_framework import serializers
from coinpricecache import models


class CoinPriceCacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoinPriceCache
        fields = '__all__'