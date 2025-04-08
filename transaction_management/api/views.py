from django.shortcuts import render
from rest_framework import generics
from .models import TransactionModel
from .serializers import TransactionSerializer


class TransactionCreate(generics.ListCreateAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer