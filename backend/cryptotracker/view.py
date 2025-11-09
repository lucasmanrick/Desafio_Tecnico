# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from utils.health_check import verify_health

class HealthCheckView(APIView):
    permission_classes = [permissions.AllowAny]      

    def get(self, request):
       try:
           response = verify_health()
           return Response (response, status=status.HTTP_200_OK)
       except Exception as e:
           return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)