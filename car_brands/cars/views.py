from rest_framework import generics
from .models import CarBrand
from .serializers import CarBrandSerializer
class CarBrandCreateView(generics.CreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarBrandDetailView(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarBrandListView(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
