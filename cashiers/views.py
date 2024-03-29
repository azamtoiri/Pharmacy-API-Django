from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from django.contrib.auth import get_user_model

from cashiers.models import Cashiers, Accounts
from cashiers.serializers import CashiersSerializer, AccountsSerializer, AccountCreateSerializer, CashiersUpdateDeleteSerializer

"""
Notes
ListCreateAPIView - [POST, GET] method on one
CreateAPIView - [POST] create something 
ListAPIView - [GET] get from db
RetrieveUpdateDestroyAPIView - [GET, PUT, UPDATE, DELETE]
"""


# region: Cashier View
class CashierCreateView(generics.CreateAPIView):
    serializer_class = CashiersSerializer
    permission_classes = (IsAdminUser,)


class CashierListView(generics.ListAPIView):
    serializer_class = CashiersSerializer
    queryset = Cashiers.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'brith_date']


class CashierDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CashiersUpdateDeleteSerializer
    permission_classes = (IsAdminUser,)
    queryset = Cashiers.objects.all()


# endregion

# region: Account View
class CreateAccountView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (IsAdminUser,)
    serializer_class = AccountCreateSerializer


class AccountListView(generics.ListAPIView):
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'is_superuser', 'is_active']


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()
    permission_classes = (IsAdminUser,)

# endregion
