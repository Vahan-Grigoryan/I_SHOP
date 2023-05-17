from rest_framework import serializers
from fapp.models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = 'image',

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = 'id', 'parent',

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = 'category', 'desc'

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    stars_avg = serializers.IntegerField()
    brand = BrandSerializer()
    comments_count = serializers.IntegerField()
    get_resolutions = serializers.JSONField()

    class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    sale_new_hit = serializers.CharField()
    stars_avg = serializers.IntegerField()
    comments_count = serializers.IntegerField()

    class Meta:
        model = Product
        exclude = 'resolution', 'optional_characteristics', 'available', 'code', 'brand', 'category', 'liked_products', 'order_products'