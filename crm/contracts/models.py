from django.db import models
from product.models import Product

class Contracts(models.Model):
    name = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cost = models.DecimalField(default=0, max_digits=8, decimal_places=2)
