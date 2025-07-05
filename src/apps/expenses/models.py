from django.db import models
from django.contrib.auth.models import User


class TransactionTypeChoice(models.TextChoices):
    CREDIT = 'CR', 'credit'
    DEBIT = 'DB', 'debit'

class TaxTypeChoice(models.TextChoices):
    FLAT = 'FL', 'flat'
    PERCENTAGE = 'PE', 'percentage'

class Expense(models.Model):
    """
    Model representing an expense.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=2,
        choices=TransactionTypeChoice.choices,
        default=TransactionTypeChoice.DEBIT
    )
    tax = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    tax_type = models.CharField(
        max_length=2,
        choices=TaxTypeChoice.choices,
        default=TaxTypeChoice.FLAT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.created_at.strftime('%Y-%m-%d')}"

