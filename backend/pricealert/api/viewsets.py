from rest_framework import viewsets, status
from rest_framework.response import Response
from pricealert.api import serializers
from pricealert import models
from coinpricecache.services.coingecko import get_coin_detail

class PriceAlertViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.PriceAlertSerializer


    def get_queryset(self):

        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data


        coin_id = data.get('coin_id')
        condition = data.get('condition')
        target_price_usd = data.get('target_price_usd')


        try:
            response = get_coin_detail(coin_id)

            if not response:
                return Response({"error": f"Não foi possivel obter dados da moeda especificada: {coin_id}"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({f"error: {e}"}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        response.get("")
        
        alert = models.PriceAlert.objects.create(
            user = user,
            coin_id = coin_id,
            coin_name = response.get("name"),
            coin_symbol = response.get("symbol"),
            condition = condition,
            target_price_usd = target_price_usd,
        )
