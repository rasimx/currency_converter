
from rest_framework import serializers

from main.models import Currency
from main.models import CurrencyRate


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyRateSerializer(serializers.ModelSerializer):
    base = CurrencySerializer(read_only=True)
    target = CurrencySerializer(read_only=True)
    
    class Meta:
        model = CurrencyRate
        fields = ['base', 'target', 'value']
        
        
        