# tasks.py
from celery import shared_task

from exernal_apis.coingecko import CoinGeckoAPI
from .models import Currency, CurrencySnapshot

@shared_task
def sync_currency_snapshot():
    params = {
        'vs_currency': 'usd'
    }
    data = CoinGeckoAPI().get('/coins/markets', params=params)

    for currency in data:
        currency_obj = Currency.objects.update_or_create(
            name=currency['name'],
            symbol=currency['symbol']
        )[0]
            
        currency_obj.save()

        snapshot = CurrencySnapshot.objects.filter(currency_id=currency_obj.id).first()
        if snapshot:
            snapshot.price=currency['current_price']
            snapshot.market_cap=currency['market_cap']
            snapshot.volume=currency['total_volume']
            snapshot.price_change_percentage_24h=currency['price_change_percentage_24h']
            snapshot.save()
        else:
            snapshot_obj = CurrencySnapshot(
                currency_id=currency_obj.id,
                price=currency['current_price'],
                market_cap=currency['market_cap'],
                volume=currency['total_volume'],
                price_change_percentage_24h=currency['price_change_percentage_24h']
            )
            snapshot_obj.save()