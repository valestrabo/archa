from django.db import models
from django.core.validators import MinValueValidator


class TransactionModel(models.Model):
    transaction_type = models.CharField(max_length=10)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.description