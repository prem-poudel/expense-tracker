from rest_framework import serializers
from .models import Expense, TaxTypeChoice

class ExpenseSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ("id", "created_at", "updated_at", "user", "total")

    def get_total(self, obj) -> float:
        """
        Calculate the total amount of the expense based on the tax type.
        """
        if obj.tax_type == TaxTypeChoice.FLAT.value:
            return obj.amount + obj.tax
        elif obj.tax_type == TaxTypeChoice.PERCENTAGE.value:
            return obj.amount + (obj.amount * (obj.tax / 100))
        return obj.amount

        