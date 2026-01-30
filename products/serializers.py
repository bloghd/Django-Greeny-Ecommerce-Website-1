
from decimal import Decimal
from rest_framework import serializers
from .models import Product, Category, Brand, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['created', 'updated']

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # brand = BrandSerializer(read_only=True)
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    # category = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='products:category_detail',

    # )
    # brand = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='products:brand_detail2',

    # )

    # price_wiht_discount = serializers.SerializerMethodField()

    price_with_clac = serializers.SerializerMethodField(method_name='get_price_with_clac')

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['slug', 'created', 'updated']


    # def get_price_wiht_discount(self, obj):
    #     if obj.discount:
    #         return obj.price - (obj.price * obj.discount / 100)
    #     return obj.price
    
    def get_price_with_clac(self, obj):
        return obj.price * Decimal('1.20')  
    

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    review = ReviewSerializer(source='reviews', many=True)

    price_with_clac = serializers.SerializerMethodField(method_name='get_price_with_clac')

    class Meta:
        model = Product
        fields = ('id', 'category', 'brand', 'name', 'sku', 'description', 'price', 'flag', 'available', 'created', 'updated', 'image', 'slug', 'stock', 'price_with_clac', 'review')
        read_only_fields = ['slug', 'created', 'updated']

    def get_price_with_clac(self, obj):
        return obj.price * Decimal('1.20')
    

# class BrandDetailSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(source='products', many=True)
#     class Meta:
#         model = Brand
#         fields = ('name', 'slug', 'product')

# class CategoryDetailSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(source='products', many=True)
#     class Meta:
#         model = Category
#         fields = ('name', 'slug', 'product')
class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='products', many=True)
    class Meta:
        model = Category
        fields = ('name', 'slug', 'product')


class BrandSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='products', many=True)
    class Meta:
        model = Brand
        fields = ('name', 'slug', 'product')

# class ReviewSerializer(serializers.ModelSerializer):
#     product = serializers.StringRelatedField()
#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ['created', 'updated']