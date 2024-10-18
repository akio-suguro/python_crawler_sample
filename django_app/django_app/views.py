from rest_framework import viewsets
from .models import ScrapedData
from .serializers import ScrapedDataSerializer

class ScrapedDataViewSet(viewsets.ModelViewSet):
    queryset = ScrapedData.objects.all()
    serializer_class = ScrapedDataSerializer
    