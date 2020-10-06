
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrenciesView
from .views import CoverterView

app_name = 'api'

urlpatterns = [
    path('', CurrenciesView.as_view(), name='list'),
    path('convert/', CoverterView.as_view(), name='convert'),
]
