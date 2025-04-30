from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from .models import Customers


class CustomersListView(ListView):
    model = Customers
    template_name = 'crm/customers/customers-list.html'
    context_object_name = 'customers'


class CustomersCreateView(CreateView):
    model = Customers
    fields = ['lead']
    template_name = 'crm/customers/customers-create.html'
    success_url = reverse_lazy('customer_list')


class CustomersDetailView(DetailView):
    model = Customers
    template_name = 'crm/customers/customers-detail.html'
    context_object_name = 'customers'


class CustomersUpdateView(UpdateView):
    model = Customers
    fields = ['lead']
    template_name = 'crm/customers/customers-edit.html'
    success_url = reverse_lazy('customer_list')


class CustomersDeleteview(DeleteView):
    model = Customers
    template_name = 'crm/customers/customers-delete.html'
    success_url = reverse_lazy('customer_list')