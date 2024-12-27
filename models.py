from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    currency = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):  # Corrected here
        return f"{self.code} - {self.currency}"

class Country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    country = models.CharField(max_length=25)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):  # Corrected here
        return f"{self.code} - {self.country}"