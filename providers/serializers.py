from rest_framework import serializers
from providers.models import Provider, Medicine


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'address', 'phone_number']


class LocalProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'address', 'phone_number']


class MedicineSerializer(serializers.ModelSerializer):
    provider = LocalProviderSerializer(many=False, read_only=True)

    class Meta:
        model = Medicine
        fields = ['id', 'name', 'amount', 'provider', 'end_date', 'provider']
