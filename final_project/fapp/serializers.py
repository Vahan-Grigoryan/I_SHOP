import re
from rest_framework import serializers
from fapp.models import *




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = 'image',

class UserForCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'photo'

class CommentSerializer(serializers.ModelSerializer):
    user = UserForCommentSerializer(read_only=True)
    class Meta:
        model = Comment
        exclude = 'product', 'id'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = 'id', 'parent',

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = 'category', 'desc'

class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = 'id', 'short_desc', 'category'

class BlogCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    stars_avg = serializers.IntegerField()
    available = serializers.BooleanField()
    brand = BrandSerializer()
    comments = CommentSerializer(many=True)
    get_resolutions = serializers.JSONField()
    category = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Product
        exclude = 'liked_in_users', 'ordered_in_orders'

class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    sale_new_hit = serializers.CharField()
    stars_avg = serializers.IntegerField()
    comments_count = serializers.IntegerField()

    class Meta:
        model = Product
        exclude = 'resolution', 'optional_characteristics', 'code', 'brand', 'category', 'liked_in_users', 'ordered_in_orders', 'quantity'

class ProductsOfCategory(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'saled_price', 'images'

class OrderSerializer(serializers.ModelSerializer):
    order_products = ProductListSerializer(many=True)
    code = serializers.CharField()
    total_prices_sum = serializers.IntegerField()
    class Meta:
        model = Order
        exclude = 'id', 'user'

class UserProfileSerializer(serializers.ModelSerializer):
    liked_products = ProductListSerializer(many=True)
    orders = OrderSerializer(many=True)
    class Meta:
        model = User
        fields = 'liked_products', 'orders'

class UserMiniInfoSerializer(serializers.ModelSerializer):
    liked_products_count = serializers.IntegerField(read_only=True)
    ordered_products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'photo',
            'liked_products_count',
            'ordered_products_count',
        )

class UserCreationSerializer(serializers.ModelSerializer):
    liked_products_count = serializers.IntegerField(read_only=True)
    ordered_products_count = serializers.IntegerField(read_only=True)

    def validate_password(self, value):
        minimum_one_number = re.search("[0-9]", value)
        if len(value) >= 8 and minimum_one_number:
            return value
        raise serializers.ValidationError("Пароль должен содержать как минимум 8 символов, одно число ")

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance



    class Meta:
        model = User
        fields = '__all__'