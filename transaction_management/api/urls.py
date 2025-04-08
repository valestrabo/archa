from django.urls import path
from . import views

urlpatterns = [
    path("transactions/", views.TransactionCreate.as_view(), name="transaction-create")
]