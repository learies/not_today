from rest_framework import viewsets

from apps.products.api.serializers import CategorySerializer
from apps.products.servises import сategories_service


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = сategories_service.get_all()
    serializer_class = CategorySerializer
