from django.urls import path, include
from .views import create_portfolio, get_portfolio, add_currency

urlpatterns = [
    path('', create_portfolio, name="create_portfolio"),
    path('<int:portfolioId>/', include([
        path('', get_portfolio, name="get_portfolio"),
        path('currencies/', include([
            path('add/', add_currency, name="add_currency")
        ]))
    ]))
]