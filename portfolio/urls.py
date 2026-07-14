from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path(
        "buy/<int:company_id>/",
        views.buy_shares,
        name="buy_shares",
    ),
]