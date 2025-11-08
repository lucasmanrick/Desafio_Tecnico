from rest_framework import serializers
from favorite import models
from coinpricecache.services.coingecko import get_coin_detail

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorite
        fields = ['id', 'coin_id', 'coin_name', 'coin_symbol', 'coin_image', 'created_at']
        read_only_fields = ['id', 'coin_name', 'coin_symbol', 'coin_image', 'created_at']

    def create(self, validated_data):
        coin_id = validated_data.get('coin_id')

        response = get_coin_detail(coin_id)
        print (response)
        if not response:
            raise serializers.ValidationError({"coin_id": "Coin not found"})

        coin_data = response
        validated_data['coin_name'] = coin_data.get("name")
        validated_data['coin_symbol'] = coin_data.get('symbol')
        validated_data['coin_image'] = coin_data.get('image', {}).get('large')


        return super().create(validated_data)