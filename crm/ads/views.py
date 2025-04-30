from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Ads
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.utils.decorators import method_decorator

from crm.decorators import group_required


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class AdsListView(ListView):
    model = Ads
    template_name = 'crm/ads/ads-list.html'
    context_object_name = 'ads'


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    fields = ['name', 'budget', 'product']
    template_name = 'crm/ads/ads-create.html'
    success_url = reverse_lazy('ads_list')


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class AdsDetailView(DetailView):
    model = Ads
    template_name = 'crm/ads/ads-detail.html'
    context_object_name = 'ads'


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ['name', 'budget', 'product']
    template_name = 'crm/ads/ads-edit.html'
    success_url = reverse_lazy('ads_list')


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    template_name = 'crm/ads/ads-delete.html'
    success_url = reverse_lazy('ads_list')


class AdsStatisticView(TemplateView):
    template_name = 'crm/ads/ads-statistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads_list = Ads.objects.all()

        for ad in ads_list:
            ad.update_statistics()

        context['ads'] = ads_list
        return context