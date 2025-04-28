from django.db import models
from product.models import Product

class Ads(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    leads_count = models.IntegerField(default=0)
    costumers_count = models.IntegerField(default=0)
    profit = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#доделать статистику и профит