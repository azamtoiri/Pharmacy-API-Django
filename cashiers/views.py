from rest_framework import generics
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser

from cashiers.models import Cashiers, Accounts
from cashiers.serializers import CashiersSerializer, AccountsSerializer, AccountCreateSerializer

"""
Notes
CreateAPIView - [POST] create something 
ListAPIView - [GET] get from db
RetrieveUpdateDestroyAPIView - [GET, PUT, UPDATE, DELETE]
"""


# region: Cashier View
class CashierCreateView(generics.CreateAPIView):
    serializer_class = CashiersSerializer
    permission_classes = (IsAdminUser, )


class CashierListView(generics.ListAPIView):
    serializer_class = CashiersSerializer
    queryset = Cashiers.objects.all()


class CashierDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CashiersSerializer
    permission_classes = (IsAdminUser, )
    queryset = Cashiers.objects.all()


# endregion

# region: Account View
class AccountCreateView(generics.CreateAPIView):
    serializer_class = AccountCreateSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)


class AccountListView(generics.ListAPIView):
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()
    permission_classes = (IsAdminUser, )

# endregion
