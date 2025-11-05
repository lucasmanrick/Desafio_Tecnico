from rest_framework import viewsets
from coinpricecache.api import serializers
from coinpricecache import models

class CoinPriceCacheViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.CoinPriceCacheSerializer
    queryset = models.CoinPriceCache.objects.all()