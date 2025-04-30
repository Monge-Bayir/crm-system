from django.urls import path
from .views import CustomersListView, CustomersCreateView, CustomersDetailView, CustomersDeleteview, CustomersUpdateView


urlpatterns = [
    path('customers/', CustomersListView.as_view(), name='customer_list'),
    path('customers/new/', CustomersCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/', CustomersDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit/', CustomersUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', CustomersDeleteview.as_view(), name='customer_delete')
]