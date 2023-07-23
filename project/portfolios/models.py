from django.db import models
from django.conf import settings

from currencies.models import Currency

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        return self.user is not None
    
class CurrencyAllocation(models.Model):
    class Meta:
        unique_together = (('currency', 'portfolio'),)

    id = models.AutoField(primary_key=True)
    portfolio = models.ForeignKey(to=Portfolio, to_field='id', related_name='portfolio', on_delete=models.CASCADE)
    currency = models.ForeignKey(to=Currency, to_field='id', related_name='currencyAllocation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        return self.portfolio is not None and self.currency is not None