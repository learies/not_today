from rest_framework import serializers

from apps.products.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'title',
            'slug',
            'preview',
            'description',
            'price',
            'image',
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'image',
            'products',
        )
