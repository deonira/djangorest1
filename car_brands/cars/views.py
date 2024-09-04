from rest_framework import generics
from .models import CarBrand
from .serializers import CarBrandSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
class CarBrandCreateView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = CarBrand.objects.all()
        serializer_class = CarBrandSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        car = get_object_or_404(CarBrand, pk=pk)
        serializer = CarBrandSerializer(car)
        return Response(serializer.data)

    def create(self, request):
        serializer_class = CarBrandSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=201)
        return Response(serializer_class.errors, status=400)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(CarBrand, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def update(self, request, pk=None):
        instance = get_object_or_404(CarBrand, pk=pk)
        serializer = CarBrandSerializer(instance, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        instance = get_object_or_404(CarBrand, pk=pk)
        serializer = CarBrandSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarBrandDetailView(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticated]

class CarBrandListView(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticated]