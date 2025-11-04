from rest_framework import serializers
from favorite import models


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorite
        fields = '__all__'