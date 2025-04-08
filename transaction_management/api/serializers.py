from rest_framework import serializers
from .models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ["id", "transaction_type", "description", "amount"]

    def validate_transaction_type(self, value):
        if not value in ["DEPOSIT", "WITHDRAW"]:
            raise serializers.ValidationError("Transaction type invalid!")
        return value