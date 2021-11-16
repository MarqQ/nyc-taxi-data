from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TaxiData
from .serializers import TaxiDataSerializer


class TaxiAPIView(APIView):
    """
    API to get taxi data
    """
    def get(self, request):
        taxi = TaxiData.objects.all()
        serializer = TaxiDataSerializer(taxi, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaxiDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
