from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Currency
from .serializers import CurrencySerializer

@api_view(['GET'])
def getAllCurrencies(request: Request):
    currencies = Currency.objects.all()
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)
