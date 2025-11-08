# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.health_check import check_database_connection, check_coingecko_api

class HealthCheckView(APIView):
    authentication_classes = []  # sem autenticação
    permission_classes = []      # acesso público

    def get(self, request):
        db_ok = check_database_connection()
        coingecko_ok = check_coingecko_api()

        status_str = "healthy" if db_ok and coingecko_ok else "unhealthy"

        return Response({
            "database": "ok" if db_ok else "error",
            "coingecko_api": "ok" if coingecko_ok else "error",
            "status": status_str
        }, status=status.HTTP_200_OK)