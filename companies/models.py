from django.db import models


class Company(models.Model):

    name = models.CharField(
        max_length=200
    )

    symbol = models.CharField(
        max_length=20,
        unique=True
    )

    yahoo_symbol = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text="Yahoo Finance ticker (e.g. AAPL, RELIANCE.NS)"
    )

    logo = models.ImageField(
        upload_to="companies/",
        blank=True,
        null=True
    )

    current_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    EXCHANGE_CHOICES = [
        ("NSE", "NSE"),
        ("BSE", "BSE"),
        ("NASDAQ", "NASDAQ"),
        ("NYSE", "NYSE"),
    ]

    exchange = models.CharField(
        max_length=20,
        choices=EXCHANGE_CHOICES,
        default="NSE",
    )

    sector = models.CharField(
        max_length=100,
        blank=True
    )

    industry = models.CharField(
        max_length=100,
        blank=True
    )

    currency = models.CharField(
        max_length=10,
        default="INR"
    )

    country = models.CharField(
        max_length=50,
        default="India"
    )

    day_change = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    day_change_percent = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    data_source = models.CharField(
        max_length=20,
        default="manual"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.symbol} - {self.name}"