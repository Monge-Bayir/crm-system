from django.urls import path

from .views import LeadsListView, LeadsCreateView, LeadsDeleteView, LeadsDetailView, LeadsUpdateView

urlpatterns = [
    path('leads/', LeadsListView.as_view(), name='lead_list'),
    path('leads/new/', LeadsCreateView.as_view(), name='lead_create'),
    path('leads/<int:pk>/', LeadsDetailView.as_view(), name='lead_detail'),
    path('leads/<int:pk>/edit/', LeadsUpdateView.as_view(), name='lead_edit'),
    path('leads/<int:pk>/delete/', LeadsDeleteView.as_view(), name='lead_delete')
]