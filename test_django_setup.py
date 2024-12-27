import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangopro.settings')
django.setup()

# Test importing your models
from world.models import Currency
currencies = Currency.objects.all()
print(currencies)
