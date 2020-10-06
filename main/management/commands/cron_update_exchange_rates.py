from django.core.management.base import BaseCommand

from main.models import Currency


class Command(BaseCommand):
    def handle(self, *args, **options):
        for currency in Currency.objects.filter(code='USD'):
            currency.update_rates()
    
   