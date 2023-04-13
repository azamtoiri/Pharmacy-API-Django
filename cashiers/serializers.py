from rest_framework import serializers
from cashiers.models import Cashiers, Accounts

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['cashiers_id', 'id', 'username', 'password', 'is_superuser', 'is_active', 'last_login']


class AccountCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('cashiers_id', 'id', 'username', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            cashiers_id=validated_data['cashiers_id'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CashiersSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cashiers
        fields = ['id', 'first_name', 'last_name', 'brith_date',
                  'phone_number', 'address', 'created_at']
