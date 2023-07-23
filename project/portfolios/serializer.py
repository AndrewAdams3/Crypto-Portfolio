from rest_framework import serializers
from . models import *
            
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = [
            "id",
            "userId",
            "created_at",
            "updated_at"
        ]


class CurrencyAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyAllocation
        fields = [
            "id",
            "portfolioId",
            "currencyId",
            "created_at",
            "updated_at"
        ]