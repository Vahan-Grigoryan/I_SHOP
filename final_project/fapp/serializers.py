import re
from rest_framework import serializers
from fapp.models import *




class ImageSerializer(serializers.ModelSerializer):
    """For other serializers(models) where one model can have 1+ images"""
    class Meta:
        model = Image
        fields = 'image',

class UserForCommentSerializer(serializers.ModelSerializer):
    """For few user info in comment"""
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
    """Fields below need for show any model functions value"""
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
        exclude = 'resolution', 'optional_characteristics', 'brand', 'category', 'liked_in_users', 'ordered_in_orders', 'quantity'

class ProductsOfCategory(serializers.ModelSerializer):
    """Few product info in similar products"""
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'saled_price', 'images'

class OrderedProductInfoSerializer(serializers.ModelSerializer):
    """Through model for view user selected options for each product"""
    total_price = serializers.IntegerField()
    def to_representation(self, instance):
        """Mix product characteristics with characteristics that can be selected"""
        selected_options = super().to_representation(instance)
        product = ProductListSerializer(instance.product).data

        return {**product, **selected_options}

    class Meta:
        model = OrderedProductInfo
        exclude = 'id', 'order'

class OrderSerializer(serializers.ModelSerializer):
    """Order with products"""
    order_products = serializers.SerializerMethodField(method_name='get_products_with_selected_options')
    code = serializers.CharField()
    total_price = serializers.IntegerField()
    payment_method_name = serializers.SlugRelatedField(source='payment_method', slug_field='name', read_only=True)
    arrive_date = serializers.SerializerMethodField(method_name='datetime_without_timezone_offset')

    def datetime_without_timezone_offset(self, instance):
        """Return datetime without timezone offset(+04:00) or None"""
        if instance.arrive_date:
            localtime = timezone.localtime(instance.arrive_date)
            return localtime.strftime('%Y-%m-%d %H:%M:%S')

    def get_products_with_selected_options(self, instance):
        return OrderedProductInfoSerializer(OrderedProductInfo.objects.filter(order=instance), many=True).data


    class Meta:
        model = Order
        exclude = 'user', 'payment_method_id', 'content_type', 'scheduled_task_id'

class SortViewedProductsSerializer(serializers.ModelSerializer):
    """Through model serializer"""

    def to_representation(self, instance):
        """Get only product without id, added_date."""
        return ProductListSerializer(instance.product).data

    class Meta:
        model = SortViewedProducts
        fields = 'product',

class UserProfileSerializer(serializers.ModelSerializer):
    liked_products = ProductListSerializer(many=True)
    orders = serializers.SerializerMethodField(method_name='get_ordered_orders')
    viewed10_products = serializers.SerializerMethodField(method_name='get_sorted_viewed10_products')

    def get_sorted_viewed10_products(self, user):
        """View sorted viewed products by through model"""
        return SortViewedProductsSerializer(
            SortViewedProducts.objects.filter(user_id=user.id).order_by('-added_date'),
            many=True
        ).data

    def get_ordered_orders(self, user):
        """Move user pending order to top"""
        return OrderSerializer(
            user.orders.order_by('-id'),
            many=True
        ).data

    class Meta:
        model = User
        fields = (
            'email',
            'tel',
            'last_name',
            'city',
            'street',
            'post_code',
            'in_mailing_list',
            'liked_products',
            'orders',
            'viewed10_products',
            'stripe_payment',
        )

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

class UserCreationUpdateSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            raw_instance = super().update(instance, validated_data)
            raw_instance.set_password(password)
            raw_instance.save()
            return raw_instance

        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = '__all__'