from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, ReviewSerializer, ProductDetailSerializer
from .models import Category, Product, Brand, Review
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticated


class Pagination20(PageNumberPagination):
    page_size = 100

# class ProductListAPI(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class CategoryListAPI(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class BrandListAPI(generics.ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer


# class ReviewListAPI(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     lookup_field = 'id'

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination20
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'price', 'available', 'flag']
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticated]

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ReviewListAPI(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPI(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


