from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets

from .models import TaxiData
from .serializers import TaxiDataSerializer


"""
API V1
"""


class TaxiAPIView(generics.ListCreateAPIView):
    queryset = TaxiData.objects.all()
    serializer_class = TaxiDataSerializer


class TaxiRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaxiData.objects.all()
    serializer_class = TaxiDataSerializer

    def get_object(self):
        if self.kwargs.get('pk'):
            return get_object_or_404(self.get_queryset(),
                                     pk=self.kwargs.get('pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))


"""
API V2
"""


class TaxiAPIViewSet(viewsets.ModelViewSet):
    queryset = TaxiData.objects.all()
    serializer_class = TaxiDataSerializer


class TaxiRetrieveAPIViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaxiData.objects.all()
    serializer_class = TaxiDataSerializer
