from django.urls import path

from .views import getAllCurrencies
urlpatterns = [
    path('', getAllCurrencies, name='list_currencies'),
]