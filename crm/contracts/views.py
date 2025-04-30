from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .models import Contracts
from django.utils.decorators import method_decorator

from crm.decorators import group_required


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class ContractListView(ListView):
    model = Contracts
    template_name = 'crm/contracts/contracts-list.html'
    context_object_name = 'contracts'


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class ContractCreateView(CreateView):
    model = Contracts
    fields = ['name', 'product', 'start_date', 'end_date', 'cost']
    template_name = 'crm/contracts/contracts-create.html'
    success_url = reverse_lazy('contract_list')


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class ContractDetailView(DetailView):
    model = Contracts
    template_name = 'crm/contracts/contracts-detail.html'


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class ContractUpdateView(UpdateView):
    model = Contracts
    fields = ['name', 'product', 'start_date', 'end_date', 'cost']
    template_name = 'crm/contracts/contracts-edit.html'
    success_url = reverse_lazy('contract_list')


@method_decorator(group_required(['manager', 'admin']), name='dispatch')
class ContractDeleteView(DeleteView):
    model = Contracts
    template_name = 'crm/contracts/contracts-delete.html'
