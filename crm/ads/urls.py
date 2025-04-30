from django.urls import path
from .views import AdsListView, AdsCreateView, AdsDetailView, AdsDeleteView, AdsUpdateView, AdsStatisticView

urlpatterns = [
    path('ads/', AdsListView.as_view(), name='ads_list'),
    path('ads/new/', AdsCreateView.as_view(), name='ads_create'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ads_detail'),
    path('ads/<int:pk>/edit/', AdsUpdateView.as_view(), name='ads_edit'),
    path('ads/<int:pk>/delete/', AdsDeleteView.as_view(), name='ads_delete'),
    path('ads/statistic/', AdsStatisticView.as_view(), name='ads_statistic')
]