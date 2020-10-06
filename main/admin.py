from django.contrib import admin

from .models import Currency
from .models import CurrencyRate


class CurrencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Currency, CurrencyAdmin)


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('base', 'target', 'date', 'value')
    fields = ('base', 'target', 'date', 'value')
    readonly_fields = ('date',)


admin.site.register(CurrencyRate, CurrencyRateAdmin)