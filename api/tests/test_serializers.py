from decimal import Decimal

from django.test import TestCase

from api.serializers import CurrencySerializer, CurrencyRateSerializer
from main.models import Currency, CurrencyRate


class ApiSerializerTestCase(TestCase):
    def test_currency(self):
        currency_1 = Currency.objects.create(code='USD', name='US dollar')
        currency_2 = Currency.objects.create(code='EUR', name='Euro')
        
        serializer_data = CurrencySerializer([currency_1, currency_2], many=True).data
        
        expected_data = [
            {
                'id': currency_1.id,
                'code': 'USD',
                'name': 'US dollar',
            },
            {
                'id': currency_2.id,
                'code': 'EUR',
                'name': 'Euro',
            }
        ]
        
        self.assertEqual(expected_data, serializer_data)
    
    def test_currency_rate(self):
        currency_1 = Currency.objects.create(code='USD', name='US dollar')
        currency_2 = Currency.objects.create(code='EUR', name='Euro')
        
        currency_rate = CurrencyRate.objects.create(base=currency_1, target=currency_2, value=Decimal(55))
        
        serializer_data = CurrencyRateSerializer([currency_rate, ], many=True).data
        expected_data = [
            {
                'base': {
                    'id': currency_1.id,
                    'code': 'USD',
                    'name': 'US dollar',
                },
                
                'target': {
                    'id': currency_2.id,
                    'code': 'EUR',
                    'name': 'Euro',
                },
                'value': '55.0000'
            }
        
        ]
        
        self.assertEqual(expected_data, serializer_data)
        
        
        
