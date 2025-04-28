from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Ads
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class AdsListView(ListView):
    model = Ads
    template_name = 'crm/ads/ads-list.html'
    context_object_name = 'ads'


class AdsCreateView(CreateView):
    model = Ads
    fields = ['name', 'budget', 'leads_count', 'costumers_count', 'profit', 'product']
    template_name = 'crm/ads/ads-create.html'
    success_url = reverse_lazy('ads_list')


class AdsDetailView(DetailView):
    model = Ads
    template_name = 'crm/ads/ads-detail.html'
    context_object_name = 'ads'


class AdsUpdateView(UpdateView):
    model = Ads
    fields = ['name', 'budget', 'leads_count', 'costumers_count', 'profit', 'product']
    template_name = 'crm/ads/ads-edit.html'
    success_url = reverse_lazy('ads_list')


class AdsDeleteView(DeleteView):
    model = Ads
    template_name = 'crm/ads/ads-delete.html'
    success_url = reverse_lazy('ads_list')

