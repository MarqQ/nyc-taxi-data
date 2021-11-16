from django.urls import path
from .views import TaxiAPIView, TaxiRetrieveAPIView


urlpatterns = [
    path('taxi_data/', TaxiAPIView.as_view(), name='taxi_data'),
    path('taxi_data/<int:pk>', TaxiRetrieveAPIView.as_view(), name='taxi_data_retrieve'),
]
