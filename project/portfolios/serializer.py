from rest_framework import serializers
from . models import *
            
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = [
            "id",
            "user",
            "created_at",
            "updated_at"
        ]


class CurrencyAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyAllocation
        fields = [
            "id",
            "currency_id",
            "portfolio_id",
            "created_at",
            "updated_at"
        ]