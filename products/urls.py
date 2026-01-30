from django.urls import path
from products.views import ProductListView, ProductDetailView, CategoryListView, BrandListView, BrandDetailView, add_favourite_product
from .api import ProductListAPI, ProductDetailAPI, CategoryListAPI, CategoryDetailAPI, BrandListAPI, BrandDetailAPI, ReviewListAPI, ReviewDetailAPI

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('brand/<slug:slug>/', BrandDetailView.as_view(), name='brand_detail'),
    path('add-favourite/', add_favourite_product, name='add_favourite_product'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),


    #url api
    path('api/cbv', ProductListAPI.as_view()),
    path('api/cbv/<int:pk>', ProductDetailAPI.as_view()),
    path('api/category/cbv', CategoryListAPI.as_view()),
    path('api/category/cbv/<int:pk>', CategoryDetailAPI.as_view()),
    path('api/brand/cbv', BrandListAPI.as_view()),
    path('api/brand/cbv/<int:pk>', BrandDetailAPI.as_view()),
    path('api/review/cbv', ReviewListAPI.as_view()),
    path('api/review/cbv/<int:id>', ReviewDetailAPI.as_view()),

]