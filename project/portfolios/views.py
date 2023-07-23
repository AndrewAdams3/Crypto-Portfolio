from django.db import transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from . models import *
from . serializer import *
  
@api_view(['GET'])
def get_portfolio(request: Request, portfolioId: int):
    portfolios = Portfolio.objects.filter(userId=portfolioId)
    serializer = PortfolioSerializer(portfolios, many=True)
    return Response(serializer.data)

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
        

@api_view(['POST'])
def add_currency(request: Request, portfolioId: int):
    newCurrencyData = {
        'portfolioId': portfolioId,
        'currencyId': request.data.get('currencyId'),
    }
    serializer = CurrencyAllocationSerializer(data=newCurrencyData)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: return Response(serializer.errors)

@api_view(['DELETE'])
def add_currency(request: Request, portfolioId: int, currencyId: int):
    currencyAllocation = CurrencyAllocation.objects.get(portfolioId=portfolioId, currencyId=currencyId)
    currencyAllocation.delete()
    
    return True