from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

from providers.models import Medicine, Provider
from providers.serializers import ProviderSerializer, MedicineSerializer, LocalProviderSerializer, \
    MedicineCreateSerializer


# region: Providers
class ProviderCreateView(generics.CreateAPIView):
    serializer_class = ProviderSerializer
    # permission_classes = ...


class ProviderListView(generics.ListAPIView):
    serializer_class = LocalProviderSerializer
    queryset = Provider.objects.all()


class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


# endregion


# region: Medicines
class MedicineCreateView(generics.CreateAPIView):
    serializer_class = MedicineCreateSerializer
    # permission_classes = ...


class MedicineListView(generics.ListAPIView):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()


class MedicineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()

# endregion"
