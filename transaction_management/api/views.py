import logging
from django.shortcuts import render
from rest_framework import generics
from .models import TransactionModel
from .serializers import TransactionSerializer

logger = logging.getLogger(__name__)


class TransactionCreate(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        if "pk" in self.kwargs:
            logger.info("Retrieving transaction with ID {}".format(self.kwargs["pk"]))
            queryset = TransactionModel.objects.filter(pk=self.kwargs["pk"])
        else:
            logger.info("Retrieving all transactions")
            queryset = TransactionModel.objects.all()
    
        return queryset