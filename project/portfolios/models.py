from django.db import models
from django.conf import settings

from currencies.models import Currency

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', db_column='userId', related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class CurrencyAllocation(models.Model):
    id = models.AutoField(primary_key=True)
    portfolioId = models.ForeignKey(to=Portfolio, to_field='id', db_column='portfolioId', related_name='portfolio', on_delete=models.CASCADE)
    currencyId = models.ForeignKey(to=Currency, to_field='id', db_column='currencyId', related_name='currencyAllocation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)