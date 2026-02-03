from django.urls import path
from products.views import ProductListView, ProductDetailView, CategoryListView, BrandListView, BrandDetailView, add_favourite_product, add_review
from .api import ProductListAPI, ProductDetailAPI, CategoryListAPI, CategoryDetailAPI, BrandListAPI, BrandDetailAPI, ReviewListAPI, ReviewDetailAPI

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('brand/<slug:slug>/', BrandDetailView.as_view(), name='brand_detail'),
    path('add-favourite/', add_favourite_product, name='add_favourite_product'),
    path('<slug:slug>/add-review/', add_review, name='add_review'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),


    #url api
    path('api/list', ProductListAPI.as_view()),
    path('api/<int:pk>', ProductDetailAPI.as_view()),
    path('api/category/', CategoryListAPI.as_view()),
    path('api/category/<int:pk>', CategoryDetailAPI.as_view(), name='category_detail'),
    path('api/brand/', BrandListAPI.as_view()),
    path('api/brand/<int:pk>', BrandDetailAPI.as_view(), name='brand_detail2'),
    path('api/review/', ReviewListAPI.as_view()),
    path('api/review/<int:id>', ReviewDetailAPI.as_view()),

]