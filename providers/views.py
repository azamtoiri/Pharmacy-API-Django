from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# from rest_framework.permissions import IsAdminUser

from providers.models import Medicine, Provider
from providers.serializers import ProviderSerializer, MedicineSerializer, LocalProviderSerializer, \
    MedicineCreateSerializer, MedicineUpdateDeleteSerializer


# region: Providers
class ProviderCreateView(generics.CreateAPIView):
    serializer_class = ProviderSerializer
    permission_classes = (IsAdminUser,)


class ProviderListView(generics.ListAPIView):
    serializer_class = LocalProviderSerializer
    queryset = Provider.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProviderSerializer
    permission_classes = (IsAdminUser,)
    queryset = Provider.objects.all()


# endregion


# region: Medicines
class MedicineCreateView(generics.CreateAPIView):
    serializer_class = MedicineCreateSerializer
    permission_classes = (IsAdminUser,)


class MedicineListView(generics.ListAPIView):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'amount']


class MedicineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicineUpdateDeleteSerializer
    permission_classes = (IsAdminUser,)
    queryset = Medicine.objects.all()

# endregion
