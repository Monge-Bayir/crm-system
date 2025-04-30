from django.db import models
from django.db.models import Sum
from product.models import Product


class Ads(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    leads_count = models.IntegerField(default=0)
    customers_count = models.IntegerField(default=0)
    profit = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def update_statistics(self):
        from leads.models import Leads
        from costumers.models import Customers
        from contracts.models import Contracts

        leads = self.leads.all()
        self.leads_count = leads.count()

        # Только те лиды, у которых есть customer
        customers = Leads.objects.filter(customers__isnull=False, ads=self)
        self.customers_count = customers.count()

        # Сумма по контрактам этих клиентов
        total_revenue = Contracts.objects.filter(
            customers__lead__ads=self
        ).aggregate(total=Sum('cost'))['total'] or 0

        self.profit = round(total_revenue - self.budget, 2)
        self.save()

    def __str__(self):
        return self.name