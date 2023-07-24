from django.db import models

class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CurrencySnapshot(models.Model):
    id = models.AutoField(primary_key=True)
    currency = models.OneToOneField(to=Currency, to_field='id', related_name='currencySnapshot', on_delete=models.CASCADE, unique=True)
    price = models.DecimalField(max_digits=30, decimal_places=16)
    price_change_percentage_24h = models.DecimalField(max_digits=30, decimal_places=16)
    market_cap = models.FloatField()
    volume = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)