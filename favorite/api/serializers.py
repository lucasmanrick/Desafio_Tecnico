from rest_framework import serializers
from favorite import models
import requests

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorite
        fields = ['id', 'coin_id', 'coin_name', 'coin_symbol', 'coin_image', 'created_at']
        read_only_fields = ['id', 'coin_name', 'coin_symbol', 'coin_image', 'created_at']

    def create(self, validated_data):
        coin_id = validated_data.get('coin_id')

        response = requests.get(f"http://localhost:8000/api/coins/{coin_id}/")
        if response.status_code != 200:
            raise serializers.ValidationError({"coin_id": "Coin not found"})

        coin_data = response.json()
        validated_data['coin_name'] = coin_data['name']
        validated_data['coin_symbol'] = coin_data['symbol']
        validated_data['coin_image'] = coin_data['image']


        return super().create(validated_data)