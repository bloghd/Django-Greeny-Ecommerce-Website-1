from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product, ProductImage, Category, Brand
from django.db.models import Count


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 50

    def get_queryset(self):
        return (
            Product.objects
    .select_related('category', 'brand')
    .prefetch_related('images')
    
        )
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context['images'] = ProductImage.objects.filter(product=myproduct)
        context['related_products'] = Product.objects.filter(category=myproduct.category).exclude(id=myproduct.id)[:10]
        return context
    
class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Category.objects.annotate(
            product_count=Count('products')
        )
        
    

class BrandListView(ListView):
    model = Brand
    template_name = 'products/brand_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Brand.objects.annotate(
            product_count=Count('products')
        )

    

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'products/brand_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Brand.objects.annotate(
            product_count=Count('products')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = (
            self.object.products
            .select_related('category')
            .prefetch_related('images')
        )
        return context

    



