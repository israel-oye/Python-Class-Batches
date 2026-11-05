from decimal import Decimal

from django.db import models


# Create your models here.
class ProductCategory(models.TextChoices):
    FASHION = ('FASH', 'Fashion')
    TECH = ('TECH', 'Technology')
    BEAUTY = ('BT', 'Beauty')
    OTHER = ('OTHER', 'Other')

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=9)
    category = models.CharField(
        choices=ProductCategory.choices,
        default=ProductCategory.OTHER,
        max_length=5
    )


