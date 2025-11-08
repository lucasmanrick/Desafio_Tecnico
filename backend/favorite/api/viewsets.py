from rest_framework import viewsets
from favorite.api import serializers
from favorite.models import Favorite
from rest_framework.permissions import IsAuthenticated

class FavoriteViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.FavoriteSerializer
    permission_classes = [IsAuthenticated]
    


    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

