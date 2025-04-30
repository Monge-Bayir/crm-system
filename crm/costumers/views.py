from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from .models import Customers
from django.utils.decorators import method_decorator

from crm.decorators import group_required


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class CustomersListView(ListView):
    model = Customers
    template_name = 'crm/customers/customers-list.html'
    context_object_name = 'customers'


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class CustomersCreateView(CreateView):
    model = Customers
    fields = ['lead', 'contract']
    template_name = 'crm/customers/customers-create.html'
    success_url = reverse_lazy('customer_list')


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class CustomersDetailView(DetailView):
    model = Customers
    template_name = 'crm/customers/customers-detail.html'
    context_object_name = 'customers'


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class CustomersUpdateView(UpdateView):
    model = Customers
    fields = ['lead']
    template_name = 'crm/customers/customers-edit.html'
    success_url = reverse_lazy('customer_list')


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class CustomersDeleteview(DeleteView):
    model = Customers
    template_name = 'crm/customers/customers-delete.html'
    success_url = reverse_lazy('customer_list')