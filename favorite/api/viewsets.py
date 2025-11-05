from rest_framework import viewsets
from favorite.api import serializers
from favorite import models

class FavoriteViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.FavoriteSerializer
    queryset = models.Favorite.objects.all()