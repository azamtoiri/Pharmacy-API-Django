from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from cashiers.models import Cashiers, Accounts
from cashiers.serializers import CashiersSerializer, AccountsSerializer


@csrf_exempt
def cashierApi(request, id=0):
    if request.method == 'GET':
        cashiers = Cashiers.objects.all()
        cashiers_serializer = CashiersSerializer(cashiers, many=True)
        return JsonResponse(cashiers_serializer.data, safe=False)

    elif request.method == 'POST':
        cashier_data = JSONParser().parse(request)
        cashier_serializer = CashiersSerializer(data=cashier_data)
        if cashier_serializer.is_valid():
            cashier_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse(cashier_serializer.errors)

    elif request.method == 'PUT':
        cashier_data = JSONParser().parse(request)
        cashier = Cashiers.objects.get(Cashiers_ID=cashier_data['id'])
        cashier_serializer = CashiersSerializer(cashier, data=cashier_data)
        if cashier_serializer.is_valid():
            cashier_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse(cashier_serializer.errors)

    elif request.method == 'DELETE':
        try:
            cashier = Cashiers.objects.get(Cashiers_ID=id)
            cashier.delete()
            return JsonResponse("Deleted Successfully!!", safe=False)
        except Cashiers.DoesNotExist as ex:
            return JsonResponse(f"Cashier does not exist\nError {ex}", safe=False)


@csrf_exempt
def accountApi(request, id=0):
    if request.method == 'GET':
        account = Accounts.objects.all()
        account_serializer = AccountsSerializer(account, many=True)
        return JsonResponse(account_serializer.data, safe=False)

    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        account_serializer = AccountsSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse(account_serializer.errors)

    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        account = Accounts.objects.get(Cashiers_ID=account_data['cashiers_id'])
        account_serializer = AccountsSerializer(account, data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse(account_serializer.errors)

    elif request.method == 'DELETE':
        try:
            account = Accounts.objects.get(Cashiers_ID=id)
            account.delete()
            return JsonResponse("Deleted Successfully!!", safe=False)
        except Accounts.DoesNotExist as ex:
            return JsonResponse(f"Account does not exist\nError {ex}", safe=False)
