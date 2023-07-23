from django.contrib import admin
from .models import Portfolio, CurrencyAllocation

admin.site.register(Portfolio)
admin.site.register(CurrencyAllocation)