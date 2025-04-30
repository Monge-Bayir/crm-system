from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Product
from django.utils.decorators import method_decorator

from crm.decorators import group_required


class IndexView(TemplateView):
    template_name = 'crm/users/index.html'

@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'crm/products/products-list.html'
    context_object_name = 'products'


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'crm/products/products-create.html'
    success_url = reverse_lazy('product_list')


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'crm/products/products-edit.html'
    success_url = reverse_lazy('product_list')


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'crm/products/products-detail.html'
    context_object_name = 'product'


@method_decorator(group_required(['marketer', 'admin']), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'crm/products/products-delete.html'
    success_url = reverse_lazy('product_list')
