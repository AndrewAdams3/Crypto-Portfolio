from django.db import transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from currencies.serializers import CurrencySerializer

from . models import *
from . serializer import *
  
@api_view(['GET'])
def get_portfolio(request: Request, portfolioId: int):
    portfolios = Portfolio.objects.filter(user_id=portfolioId)
    response = []
    for portfolio in portfolios:
        currencies = CurrencyAllocation.objects.select_related('currency').filter(portfolio_id=portfolio.id)
        print(currencies)
        currencySerializer = CurrencySerializer(map(lambda x: x.currency, currencies), many=True)
        portfolioSerializer = PortfolioSerializer(portfolio)
        response.append({
            'portfolio': portfolioSerializer.data,
            'currencies': currencySerializer.data
        })

    return Response(response)

@api_view(['POST'])
def create_portfolio(request: Request):
    currencyAllocations = request.data.get('currencies')
    if not currencyAllocations: 
        return Response({"error": "No currencies provided"}, status=400)
    if len(currencyAllocations) < 5: 
        return Response({"error": "At least 5 currencies are required"}, status=400)
         
    try:
        with transaction.atomic():
            # Save portfolio
            portfolioSerializer = PortfolioSerializer(data=request.data.get('portfolio'))
            if portfolioSerializer.is_valid():        
                portfolioSerializer.save()
            else: return Response(portfolioSerializer.errors)

            # Save currency allocations, mapping portfolio ID into the list
            currencyData: list[CurrencyAllocation] = [{
                'portfolioId': portfolioSerializer.data['id'],
                'currencyId': currency['currencyId'],
            } for currency in currencyAllocations]

            currencySerializer = CurrencyAllocationSerializer(data=currencyData, many=True)
            if currencySerializer.is_valid():
                currencySerializer.save()
                return Response(portfolioSerializer.data)
            else: return Response(currencySerializer.errors)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
        

@api_view(['POST', 'DELETE'])
def handle_currency(request: Request, portfolioId: int):
    if request.method == 'POST':
        return add_currency(request, portfolioId, request.data.get('currencyId'))
    elif request.method == 'DELETE':
        return remove_currency(request, portfolioId, request.data.get('currencyId'))
    
def add_currency(request: Request, portfolioId: int, currencyId):
    newCurrencyAllocation = CurrencyAllocation(
        portfolio_id=portfolioId, 
        currency_id=currencyId
    )
    newCurrencyAllocation.save()

    return Response(True, status=200)

def remove_currency(request: Request, portfolioId: int, currencyId: int):
    currencyAllocation = CurrencyAllocation.objects.get(portfolio_id=portfolioId, currency_id=currencyId)
    currencyAllocation.delete()
    return Response(True, status=200)