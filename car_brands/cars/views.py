from rest_framework import generics
from .models import CarBrand
from .serializers import CarBrandSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class CarBrandCreateView(generics.CreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarBrandDetailView(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticated]

class CarBrandListView(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticated]