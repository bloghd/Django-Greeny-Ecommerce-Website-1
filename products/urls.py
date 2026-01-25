from django.urls import path
from products.views import ProductListView, ProductDetailView, CategoryListView, BrandListView, BrandDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('brand/<slug:slug>/', BrandDetailView.as_view(), name='brand_detail'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]