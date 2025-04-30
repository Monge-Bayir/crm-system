from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Product


class IndexView(TemplateView):
    template_name = 'crm/users/index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'crm/products/products-list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'crm/products/products-create.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'crm/products/products-edit.html'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'crm/products/products-detail.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'crm/products/products-delete.html'
    success_url = reverse_lazy('product_list')
