from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TaxiAPIView, TaxiRetrieveAPIView, TaxiAPIViewSet, TaxiRetrieveAPIViewSet


router = SimpleRouter()
router.register('taxi_data', TaxiAPIViewSet)


urlpatterns = [
    path('taxi_data/', TaxiAPIView.as_view(), name='taxi_data'),
    path('taxi_data/<int:pk>', TaxiRetrieveAPIView.as_view(), name='taxi_data_retrieve'),
]
