from django.urls import path, include
from .views import create_portfolio, get_portfolio, handle_currency, get_metrics

urlpatterns = [
    path('', create_portfolio, name="create_portfolio"),
    path('<int:portfolioId>/', include([
        path('', get_portfolio, name="get_portfolio"),
        path('currencies/', handle_currency, name="handle_currency"),
        path('metrics/', get_metrics, name="get_metrics"),
    ]))
]