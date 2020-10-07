from datetime import date

from django.db import models
# Create your models here.

from .services import get_rates


class Currency(models.Model):
    code = models.CharField('code', max_length=3)
    name = models.CharField('name', max_length=55)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
    
    def update_rates(self):
        rates = get_rates(self.code)
        
        other_currencies = self.__class__.objects.exclude(code=self.code)
        
        for currency in other_currencies:
            if not CurrencyRate.objects.filter(base=self, target=currency, date=date.today()).exists():
                CurrencyRate.objects.create(base=self, target=currency, value=rates[currency.code])
    

class CurrencyRate(models.Model):
    base = models.ForeignKey(Currency, related_name='base_rates', on_delete=models.CASCADE)
    target = models.ForeignKey(Currency, related_name='target_rates', on_delete=models.CASCADE)
    date = models.DateField('date', auto_now_add=True)
    value = models.DecimalField('Value', max_digits=9, decimal_places=4)
    
    def __str__(self):
        return '{base} --> {target}'.format(base=self.base.code, target=self.target.code)
    
    class Meta:
        verbose_name = 'Currency rate'
        verbose_name_plural = 'Currency rates'
        unique_together = ["base", "target", "date"]