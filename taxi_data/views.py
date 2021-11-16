from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import TaxiData
from .serializers import TaxiDataSerializer


class TaxiAPIView(generics.ListCreateAPIView):
    queryset = TaxiData.objects.all()[:10]
    serializer_class = TaxiDataSerializer


class TaxiRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaxiData.objects.all()
    serializer_class = TaxiDataSerializer

    def get_object(self):
        if self.kwargs.get('pk'):
            return get_object_or_404(self.get_queryset(),
                                     pk=self.kwargs.get('pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))
