from rest_framework import serializers
from cashiers.models import Cashiers, Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['accounts_id', 'login']


class CashiersSerializer(serializers.ModelSerializer):
    cashiers_id = AccountsSerializer(many=True, read_only=True)

    class Meta:
        model = Cashiers
        fields = ['id', 'first_name', 'last_name', 'brith_date',
                  'phone_number', 'address', 'created_at', 'cashiers_id']
