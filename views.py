from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from world.models import Currency

def get_currency(request):
    currency_code = "USD"
    try:
        currency_data = Currency.objects.get(code=currency_code)
        return HttpResponse(f'Currency: {currency_data}')
    except Currency.DoesNotExist:
        return HttpResponse('Currency not found.')