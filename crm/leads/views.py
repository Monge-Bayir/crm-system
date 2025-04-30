from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Leads
from django.utils.decorators import method_decorator

from crm.decorators import group_required


@method_decorator(group_required(['operator', 'admin']), name='dispatch')
class LeadsListView(ListView):
    model = Leads
    template_name = 'crm/leads/leads-list.html'
    context_object_name = 'leads'


@method_decorator(group_required(['operator', 'admin']), name='dispatch')
class LeadsCreateView(CreateView):
    model = Leads
    fields = ['last_name', 'first_name', 'phone', 'email']
    template_name = 'crm/leads/leads-create.html'
    success_url = reverse_lazy('lead_list')


@method_decorator(group_required(['operator', 'admin']), name='dispatch')
class LeadsUpdateView(UpdateView):
    model = Leads
    fields = ['last_name', 'first_name', 'phone', 'email']
    template_name = 'crm/leads/leads-edit.html'
    success_url = reverse_lazy('lead_list')


@method_decorator(group_required(['operator', 'admin']), name='dispatch')
class LeadsDetailView(DetailView):
    model = Leads
    template_name = 'crm/leads/leads-detail.html'
    context_object_name = 'leads'


@method_decorator(group_required(['operator', 'admin']), name='dispatch')
class LeadsDeleteView(DeleteView):
    model = Leads
    template_name = 'crm/leads/leads-delete.html'
    success_url = reverse_lazy('lead_list')