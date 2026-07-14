from django.db import models
from django.conf import settings
from companies.models import Company

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolios"
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="portfolios"
    )
    quantity = models.PositiveIntegerField()
    average_buy_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "portfolios"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.company.symbol}"
    