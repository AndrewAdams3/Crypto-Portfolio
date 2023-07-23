from django.db import models

class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class CurrencySnapshot(models.Model):
    id = models.AutoField(primary_key=True)
    currencyId = models.ForeignKey(to=Currency, to_field='id', db_column='currencyId', related_name='currencySnapshot', on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    market_cap = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)