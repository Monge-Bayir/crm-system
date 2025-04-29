from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Leads


class LeadsListView(ListView):
    model = Leads
    template_name = 'crm/leads/leads-list.html'
    context_object_name = 'leads'


class LeadsCreateView(CreateView):
    model = Leads
    fields = ['last_name', 'first_name', 'phone', 'email']
    template_name = 'crm/leads/leads-create.html'
    success_url = reverse_lazy('lead_list')


class LeadsUpdateView(UpdateView):
    model = Leads
    fields = ['last_name', 'first_name', 'phone', 'email']
    template_name = 'crm/leads/leads-edit.html'
    success_url = reverse_lazy('lead_list')


class LeadsDetailView(DetailView):
    model = Leads
    template_name = 'crm/leads/leads-detail.html'
    context_object_name = 'leads'


class LeadsDeleteView(DeleteView):
    model = Leads
    template_name = 'crm/leads/leads-delete.html'
    success_url = reverse_lazy('lead_list')