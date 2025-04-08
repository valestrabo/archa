from rest_framework.test import APITestCase
from django.urls import reverse
from .models import TransactionModel


class TransactionModelTestCase(APITestCase):
    def setUp(self):
        TransactionModel.objects.create(transaction_type="DEPOSIT", 
                                        description="Initial deposit", 
                                        amount=100.00)
        TransactionModel.objects.create(transaction_type="WITHDRAW", 
                                        description="Initial withdraw", 
                                        amount=100.00)

    def test_transactions(self):
        deposit = TransactionModel.objects.get(id=1)
        withdraw = TransactionModel.objects.get(id=2)
        self.assertEqual(deposit.description, "Initial deposit")
        self.assertEqual(withdraw.description, "Initial withdraw")

class TransactionEndpoitTestCase(APITestCase):
    def setUp(self):
        self.data = {"id": 1,
                     "transaction_type": "DEPOSIT", 
                     "description": "Test", 
                     "amount": "100.00"}

    def test_create_transaction(self):
        response = self.client.post(reverse("transaction-create"), self.data)
        self.assertEqual(response.status_code, 201)

    def test_get_all_transactions(self):
        self.client.post(reverse("transaction-create"), self.data)
        response = self.client.get(reverse("transaction-create"))
        self.assertEqual(response.data[0], self.data)

    def test_get_transaction_by_id(self):
        self.client.post(reverse("transaction-create"), self.data)
        response = self.client.get(reverse("transaction-create"), {"pk": 1})
        self.assertEqual(response.data[0], self.data)
