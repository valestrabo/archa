from django.shortcuts import render
from rest_framework import generics
from .models import TransactionModel
from .serializers import TransactionSerializer


class TransactionCreate(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        if "pk" in self.kwargs:
            queryset = TransactionModel.objects.filter(pk=self.kwargs["pk"])
        else:
            queryset = TransactionModel.objects.all()
    
        return queryset