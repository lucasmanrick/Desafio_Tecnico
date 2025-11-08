from decimal import Decimal
from datetime import datetime
import requests

from rest_framework import viewsets, status
from rest_framework.response import Response

from portfolioholding.api import serializers
from portfolioholding import models
from portfolioholding.tasks import update_portfolio_prices
from coinpricecache.services.coingecko import get_coin_detail

class PortfolioHoldingViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.PortfolioHoldingSerializer

    def get_queryset(self):
        return models.PortfolioHolding.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Sobrescreve o GET /api/portfolio/
        para retornar o portfólio sincronizado.
        """
        user = request.user
        data = update_portfolio_prices(user.id)
        return Response(data)   

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        coin_id = data.get("coin_id")
        amount = Decimal(str(data.get("amount", 0)))
        purchase_price_usd = Decimal(str(data.get("purchase_price_usd", 0)))
        purchase_date = data.get("purchase_date")

        if not coin_id or not amount or not purchase_price_usd or not purchase_date:
            return Response(
                {"error": "Campos obrigatórios: coin_id, amount, purchase_price_usd, purchase_date"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            coin_data = get_coin_detail(coin_id, vs_currency="usd")
            if not coin_data:
                return Response({"error": f"Não foi possível obter dados da moeda '{coin_id}'."},
                            status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            return Response({"error": f"Erro ao buscar dados da moeda: {str(e)}"}, status=500)

        # 🔹 Preenche campos automáticos
        coin_name = coin_data.get("name")
        coin_symbol = coin_data.get("symbol")
        coin_image = coin_data.get("image", {}).get("large") or coin_data.get("image")
        current_price_usd = Decimal(str(coin_data.get("market_data", {}).get("current_price", {}).get("usd", 0)))

        invested_value = amount * purchase_price_usd
        current_value = amount * current_price_usd
        profit = current_value - invested_value
        profit_percentage = (profit / invested_value * 100) if invested_value > 0 else 0

        # 🔹 Cria registro no banco
        holding = models.PortfolioHolding.objects.create(
            user=user,
            coin_id=coin_id,
            coin_name=coin_name,
            coin_symbol=coin_symbol,
            coin_image=coin_image,
            amount=amount,
            purchase_price_usd=purchase_price_usd,
            purchase_date=purchase_date
        )

        response_json = {
        "id": str(holding.id),
        "coin_id": holding.coin_id,
        "coin_name": holding.coin_name,
        "coin_symbol": holding.coin_symbol,
        "coin_image": holding.coin_image,
        "amount": float(round(holding.amount, 10)),
        "purchase_price_usd": float(round(holding.purchase_price_usd, 2)),
        "current_price_usd": float(round(current_price_usd, 2)),
        "invested_value_usd": float(round(invested_value, 2)),
        "current_value_usd": float(round(current_value, 2)),
        "profit_usd": float(round(profit, 2)),
        "profit_percentage": round(float(profit_percentage), 2),
        "purchase_date": holding.purchase_date.isoformat() + "Z",
        "created_at": holding.created_at.isoformat() + "Z",
        "updated_at": holding.updated_at.isoformat() + "Z",
    }
        


        return Response(response_json, status=status.HTTP_201_CREATED)