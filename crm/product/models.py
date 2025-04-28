from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    cost = models.DecimalField(default=0, max_digits=8, decimal_places=2)