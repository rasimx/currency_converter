from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import CurrencyRateSerializer
from main.models import CurrencyRate, Currency


class CurrenciesViewTestCase(APITestCase):
    def test_get(self):
        url = reverse('api:list')
        currency_1 = Currency.objects.create(code='USD', name='US dollar')
        currency_2 = Currency.objects.create(code='EUR', name='Euro')
        currency_rate = CurrencyRate.objects.create(base=currency_1, target=currency_2, value=Decimal(0.85))
        response = self.client.get(url)
        serializer_data = CurrencyRateSerializer([currency_rate,], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class CoverterViewTestCase(APITestCase):
    def test_post(self):
        url = reverse('api:convert')
        currency_1 = Currency.objects.create(code='USD', name='US dollar')
        currency_2 = Currency.objects.create(code='EUR', name='Euro')
        currency_rate = CurrencyRate.objects.create(base=currency_1, target=currency_2, value=Decimal(0.85))
        
        response = self.client.post(url, {
            'base_currency': 'USD',
            'target_currency': 'EUR',
            'value': '10'
        })
        expected_data = {
            'success': True,
            'result': Decimal('8.5000')
        }

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)