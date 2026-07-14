from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path(
        "buy/<int:company_id>/",
        views.buy_shares,
        name="buy_shares",
    ),
    path(
        "",
        views.portfolio_list,
        name="portfolio_list",
    ),
    path(
        "sell/<int:portfolio_id>/",
        views.sell_shares,
        name="sell_shares",
    ),
]