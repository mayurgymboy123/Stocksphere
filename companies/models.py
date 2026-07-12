from django.db import models

class Company(models.Model):
    name = models.CharField(
        max_length=255
    )

    symbol = models.CharField(
        max_length=20,
        unique=True
    )

    logo = models.ImageField(
        upload_to="company_logos/",
        blank=True,
        null=True
    )

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
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

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"{self.symbol} - {self.name}"