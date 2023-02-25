from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from cashiers.models import Cashiers
from cashiers.serializers import CashiersSerializer


class CashierAPIViewTest(TestCase):

    def setUp(self):
        self.url = reverse('create_cashiers')
        self.url2 = reverse('get_cashiers')
        self.my_model = Cashiers.objects.create(
            first_name='Test name', last_name='test last name', brith_date='2007-12-02',
            phone_number='+7956511315', address='Moscow str. tverskaya d 12'
        )

    def test_create_model(self):
        data = {'first_name': 'Test name', 'last_name': 'Test last Name', 'brith_date': '2007-12-02',
                'phone_number': '+7956511315', 'address': 'Moscow str. tverskaya d 12'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cashiers.objects.last().first_name, data['first_name'])
        self.assertEqual(Cashiers.objects.last().last_name, data['last_name'])

    def test_get_all_models(self):
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.my_model.first_name)
        self.assertEqual(response.data[0]['last_name'], self.my_model.last_name)
