from django.db import connection, transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from . models import *
from . serializer import *

@api_view(['GET'])
def get_portfolio(_: Request, portfolioId: int):
    portfolios = Portfolio.objects.filter(user_id=portfolioId)
    response = []
    for portfolio in portfolios:
        currencyAllocations =  CurrencyAllocation.objects.select_related('currency').filter(portfolio_id=portfolio.id)
        currencies = []
        for allocatedCurrency in currencyAllocations:
            currency = {
                'id': allocatedCurrency.currency.id,
                'name': allocatedCurrency.currency.name,
                'symbol': allocatedCurrency.currency.symbol
            }
            currencies.append(currency)

        portfolioSerializer = PortfolioSerializer(portfolio)
        response.append({
            'portfolio': portfolioSerializer.data,
            'currencies': currencies
        })

    return Response(response)

@api_view(['POST'])
def create_portfolio(request: Request):
    currencyAllocations = request.data.get('currencies')
    portfolio = request.data.get('portfolio')

    if not currencyAllocations: 
        return Response({"error": "No currencies provided"}, status=400)
    if len(currencyAllocations) < 5: 
        return Response({"error": "At least 5 currencies are required"}, status=400)
         
    try:
        with transaction.atomic():
            # Save portfolio
            newPortfolio = Portfolio(user_id=portfolio['userId'])
            if newPortfolio.is_valid():        
                newPortfolio.save()
            else: return Response("Invalid Portfolio", status=400)

            # Save currency allocations, mapping portfolio ID into the list
            currencyData: list[CurrencyAllocation] = [{
                'portfolio_id': newPortfolio.id,
                'currency_id': currency['currencyId'] 
            } for currency in currencyAllocations]
        
            for currency in currencyData:
                newCurrency = CurrencyAllocation(
                    currency_id=currency['currency_id'],
                    portfolio_id=currency['portfolio_id']
                )

                if newCurrency.is_valid(): 
                    newCurrency.save()
                else: return Response("Invalid Currency", status=400)
            
            response = PortfolioSerializer(newPortfolio)
            return Response(response.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
        

@api_view(['POST', 'DELETE'])
def handle_currency(request: Request, portfolioId: int):
    if request.method == 'POST':
        return add_currency(request, portfolioId, request.data.get('currencyId'))
    elif request.method == 'DELETE':
        return remove_currency(request, portfolioId, request.data.get('currencyId'))
    
def add_currency(_: Request, portfolioId: int, currencyId):
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


@api_view(['GET'])
def get_metrics(_: Request, portfolioId: int):
    with connection.cursor() as cursor:
        query = f'''
            select c.name, c.symbol, ca.currency_id, cs.market_cap, cs.price, cs.volume, cs.price_change_percentage_24h from portfolios_currencyallocation as ca
            left join currencies_currency as c on c.id = ca.currency_id
            left join currencies_currencysnapshot as cs on ca.currency_id = cs.currency_id
            where ca.portfolio_id = %s
        '''
        cursor.execute(query, [portfolioId])
        rows = cursor.fetchall()

        currencies = []
        for column in rows:
            currency = {
                'id': column[2],
                'name': column[0],
                'symbol': column[1],
                'market_cap': column[3],
                'price': column[4],
                'volume': column[5],
                'price_change_percentage_24h': column[6]
            }
            currencies.append(currency)

        totalVolume = 0
        highestTradingVolume = None
        for currency in currencies:
            totalVolume += currency['volume']
            if not highestTradingVolume or currency['volume'] > highestTradingVolume['volume']:
                highestTradingVolume = currency
        
        return Response({
            'currencies': currencies,
            'totalVolume': totalVolume,
            'highestTradingVolume': highestTradingVolume
        })
