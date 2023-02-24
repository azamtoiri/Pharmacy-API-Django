from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from providers.models import Provider, Medicine
from providers.serializers import ProviderSerializer, MedicineSerializer


@csrf_exempt
def providerApi(request, id=0):
    if request.method == 'GET':
        providers = Provider.objects.all()
        providers_serializer = ProviderSerializer(providers, many=True)
        return JsonResponse(providers_serializer.data, safe=False)

    elif request.method == 'POST':
        provider_data = JSONParser().parse(request)
        providers_serializer = ProviderSerializer(data=provider_data)
        if providers_serializer.is_valid():
            providers_serializer.save()
            return JsonResponse(provider_data)
        return JsonResponse(providers_serializer.errors)

    elif request.method == 'PUT':
        provider_data = JSONParser().parse(request)
        provider = Provider.objects.get(Provider_ID=provider_data['id'])
        providers_serializer = ProviderSerializer(provider, data=provider_data)
        if providers_serializer.is_valid():
            providers_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse(providers_serializer.errors)

    elif request.method == 'DELETE':
        try:
            provider = Provider.objects.get(Provider_ID=id)
            provider.delete()
            return JsonResponse("Deleted Successfully!!", safe=False)
        except Provider.DoesNotExist as ex:
            return JsonResponse(f"Provider does not exist\nError {ex}", safe=False)


@csrf_exempt
def medicine_api(request, id=0):
    if request.method == 'GET':
        medicines = Medicine.objects.all()
        medicines_serializer = MedicineSerializer(medicines, many=True)
        return JsonResponse(medicines_serializer.data, safe=False)

    elif request.method == 'POST':
        medicine_data = JSONParser().parse(request)
        medicines_serializer = MedicineSerializer(data=medicine_data)
        if medicines_serializer.is_valid():
            medicines_serializer.save()
            return JsonResponse(medicine_data)
        return JsonResponse(medicines_serializer.errors)

    elif request.method == 'PUT':
        medicine_data = JSONParser().parse(request)
        medicine = Medicine.objects.get(Medicine_ID=medicine_data['id'])
        medicines_serializer = MedicineSerializer(medicine, data=medicine_data)
        if medicines_serializer.is_valid():
            medicines_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse(medicines_serializer.errors)

    elif request.method == 'DELETE':
        try:
            medicine = Medicine.objects.get(Medicine_ID=id)
            medicine.delete()
            return JsonResponse("Deleted Successfully!!", safe=False)
        except Medicine.DoesNotExist as ex:
            return JsonResponse(f"Medicine does not exist\nError {ex}", safe=False)

