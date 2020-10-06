from decimal import Decimal

from django.test import TestCase

from main.services import get_rates


class GetRatesTest(TestCase):
    
    def test_request_api(self):
        rates = get_rates('USD')
        self.assertIn('EUR', rates)


