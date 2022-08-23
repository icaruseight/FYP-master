from .views import PriceView 

from django.urls import path

urlpatterns = [
    path('api/pricing', PriceView.as_view(), name='pricing'),
]