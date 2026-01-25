from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product, ProductImage, Category, Brand


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 2
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querset = self.get_object()
        context['images'] = ProductImage.objects.filter(product=querset)
        return context
    
class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    paginate_by = 2

class BrandListView(ListView):
    model = Brand
    template_name = 'products/brand_list.html'
    paginate_by = 2

    

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context['products'] = Product.objects.filter(brand=brand)
        return context



