# tasks.py
from celery import shared_task
from .models import Currency, CurrencySnapshot
import requests

class CoinGeckoData:
    id: str
    symbol: str
    name: str
    image: str
    current_price: str
    market_cap: str
    market_cap_rank: str
    fully_diluted_valuation: str
    total_volume: str
    high_24h: str
    low_24h: str
    price_change_24h: str
    price_change_percentage_24h: str
    market_cap_change_24h: str
    market_cap_change_percentage_24h: str
    circulating_supply: str
    total_supply: str
    max_supply: str
    ath: str
    ath_change_percentage: str
    ath_date: str
    atl: str
    atl_change_percentage: str
    atl_date: str
    roi: str
    last_updated: str

@shared_task
def sync_currency_snapshot():
    data: list[CoinGeckoData] = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd").json()

    for currency in data:
        currency_obj, created = Currency.objects.update_or_create(
            name=currency['name'],
            symbol=currency['symbol']
        )

        if created:
            print("Added new currency " + currency['name'] + " (" + currency['symbol'] + ")")
            
        snapshot_obj, created = CurrencySnapshot.objects.update_or_create(
            currencyId=currency_obj,
            price=currency['current_price'],
            market_cap=currency['market_cap'],
            volume=currency['total_volume'],
        )

        currency_obj.save()
        snapshot_obj.save()
