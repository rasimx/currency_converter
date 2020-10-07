from datetime import date
from decimal import Decimal

from django.test import TestCase

from main.models import Currency, CurrencyRate
from main.services import get_rates


class CurrencyModelTest(TestCase):
    
    def test_string_representation(self):
        currency = Currency(code="USD", name='US Dollar')
        self.assertEqual(str(currency), currency.name)
        
    def test_update_rates(self):
        currency_1 = Currency.objects.create(code='USD', name='US dollar')
        currency_2 = Currency.objects.create(code='EUR', name='Euro')
        currency_1.update_rates()

        rates = CurrencyRate.objects.filter(base=currency_1, target=currency_2, date=date.today())
        
        self.assertEqual(1, rates.count())
        

class CurrencyRateModelTest(TestCase):
    
    def test_string_representation(self):
        currency_1 = Currency.objects.create(code='USD', name='US dollar')
        currency_2 = Currency.objects.create(code='EUR', name='Euro')
        currency_rate = CurrencyRate.objects.create(base=currency_1, target=currency_2, value=Decimal(0.85))
        
        self.assertEqual('USD --> EUR', str(currency_rate))