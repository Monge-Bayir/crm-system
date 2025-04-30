from django.db import models
from leads.models import Leads


class Customers(models.Model):
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE)
