from rest_framework import generics
from cashiers.serializers import CashiersSerializer, AccountsSerializer, AccountCreateSerializer
from cashiers.models import Cashiers, Accounts

"""
Notes
CreateAPIView - [POST] create something 
ListAPIView - [GET] get from db
RetrieveUpdateDestroyAPIView - [GET, PUT, UPDATE, DELETE]
"""


# region: Cashier View
class CashierCreateView(generics.CreateAPIView):
    serializer_class = CashiersSerializer


class CashierListView(generics.ListAPIView):
    serializer_class = CashiersSerializer
    queryset = Cashiers.objects.all()


class CashierDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CashiersSerializer
    queryset = Cashiers.objects.all()


# endregion

# region: Account View
class AccountCreateView(generics.CreateAPIView):
    serializer_class = AccountCreateSerializer
    queryset = Accounts.objects.all()


class AccountListView(generics.ListAPIView):
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()

# endregion
