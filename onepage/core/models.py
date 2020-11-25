from django.db import models

class TaxCalculator(models.Model):
    salary = models.CharField(max_length=200)
    PERSONAL_ALLOWANCE = 'Personal Allowance'
    BASIC_RATE = 'Basic Rate'
    HIGHER_RATE = 'Higher Rate'
    ADDITIONAL_RATE = 'Additional Rate'

    BAND_CHOICES = [
        (PERSONAL_ALLOWANCE, 'Personal Allowance'),
        (BASIC_RATE, 'Basic Rate'),
        (HIGHER_RATE, 'Higher Rate'),
        (ADDITIONAL_RATE, 'Additional Rate'),
    ]
    bands = models.CharField(
        max_length=200,
        choices= BAND_CHOICES,
        default= BASIC_RATE)

