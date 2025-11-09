from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from coinpricecache.services.coingecko import get_top_coins, get_coin_detail, get_coin_chart


class CoinListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        page = int(request.query_params.get("page", 1))
        per_page = int(request.query_params.get("per_page", 20))
        vs_currency = request.query_params.get("vs_currency", "usd")

        if per_page > 100:
            per_page = 100  # força limite da CoinGecko
        elif page * per_page > 100:
            page = 1 #se a pessoa tentar pedir pagina que no final dariam mais que as top 100 moedas nós trazemos só a quantidade que ele solicitou sem a paginação.


        data = get_top_coins(per_page=per_page, vs_currency=vs_currency, page=page)
        if not data:
            return Response({"detail": "Erro ao buscar dados da CoinGecko"}, status=status.HTTP_502_BAD_GATEWAY)

        return Response(data, status=status.HTTP_200_OK)


class CoinDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, coin_id: str):
        data = get_coin_detail(coin_id)
        if not data:
            return Response({"detail": "Moeda não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data, status=status.HTTP_200_OK)


class CoinChartView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, coin_id: str):
        vs_currency = request.query_params.get("vs_currency", "usd")
        days = int(request.query_params.get("days", 1))  # 1 dia padrão
        data = get_coin_chart(coin_id, vs_currency, days)
        if not data:
            return Response({"detail": "Gráfico não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data, status=status.HTTP_200_OK)