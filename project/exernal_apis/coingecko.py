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

class CoinGeckoAPI:
    def __init__(self):
        self.base_url = 'https://api.coingecko.com/api/v3'

    def get(self, path: str = '/coins/markets', params: dict = {}) -> list[CoinGeckoData]:
        return requests.get(self.base_url + path, params=params).json()