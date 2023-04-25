from rest_framework import viewsets

from apps.products.api.serializers import CategorySerializer, ProductSerializer
from apps.products.servises import products_service, сategories_service


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = сategories_service.get_all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = products_service.get_all()
    serializer_class = ProductSerializer
