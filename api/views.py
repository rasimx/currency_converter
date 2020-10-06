from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import authentication_classes, permission_classes

from datetime import date
import decimal

from .serializers import CurrencyRateSerializer

from main.models import Currency
from main.models import CurrencyRate

@authentication_classes([])
@permission_classes([])
class CurrenciesView(APIView):
    serializer_class = CurrencyRateSerializer
    
    def get(self, request):
        base = Currency.objects.get(code='USD')

        rates = CurrencyRate.objects.filter(base=base, date=date.today())
        serializer = CurrencyRateSerializer(rates, many=True)
        return Response(serializer.data)


class CoverterView(APIView):
    
    def post(self, request):
        base_currency = request.data.get('base_currency')
        target_currency = request.data.get('target_currency')
        value = request.data.get('value')
        
        rate = CurrencyRate.objects.get(base__code=base_currency, target__code=target_currency, date=date.today())
        
        result = decimal.Decimal(value) * rate.value
        
        return Response({"success": True, "result": result})

