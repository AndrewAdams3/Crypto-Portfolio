from django.db import models

class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CurrencySnapshot(models.Model):
    id = models.AutoField(primary_key=True)
    currency = models.OneToOneField(to=Currency, to_field='id', related_name='currencySnapshot', on_delete=models.CASCADE, unique=True)
    price = models.CharField(max_length=255)
    market_cap = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)