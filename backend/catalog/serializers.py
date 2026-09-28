from . import models
from rest_framework import serializers


# FOR CATEGORY MODEL
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "name", "slug"]


# FOR PRODUCT VARIANT MODEL
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductVariant
        fields = ["id", "name", "price", "in_stock"]


# SERIALIZER FOR PRODUCT LIST
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "name", "category", "slug", "created_at"]


# SERIALIZER FOR PRODUCT LIST
class ProductDetailSerializer(serializers.ModelSerializer):

    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "slug",
            "created_at",
            "variants",
        ]
