import uuid
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

    order_id = models.ForeignKey(
        'Order',
        on_delete=models.SET_NULL, 
        null=True,
        related_name='products'
    )

    class Meta:
        ordering = ['-name',]
        indexes =[ 
            models.Index(fields=['id', 'name']),
        ]

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category
        }


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
