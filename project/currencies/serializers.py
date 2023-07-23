from rest_framework import serializers

from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', 'created_at')

class CurrencySnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'currency', 'price', 'market_cap', 'volume', 'updated_at')