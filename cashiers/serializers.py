from rest_framework import serializers
from cashiers.models import Cashiers, Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['accounts_id', 'login']


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['cashiers_id', 'login', 'password']


class CashiersSerializer(serializers.ModelSerializer):
    cashiers_id = AccountsSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cashiers
        fields = ['id', 'first_name', 'last_name', 'brith_date',
                  'phone_number', 'address', 'created_at', 'cashiers_id', 'user']
