from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from products.models import Product, ProductImage, Category, Brand,Review
from django.db.models import Count
from accounts.models import Profile


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
        queryset = self.get_object()
        context['images'] = ProductImage.objects.filter(product=queryset)
        context['related_products'] = Product.objects.filter(category=queryset.category).exclude(id=queryset.id)[:10]
        context['reviews'] = Review.objects.filter(product=queryset)
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


def add_favourite_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        profile, created = Profile.objects.get_or_create(user=request.user)
        if product in profile.favourite_products.all():
            profile.favourite_products.remove(product)
            message = 'Product removed from favourites.'
        else:
            profile.favourite_products.add(product)
            message = 'Product added to favourites.'
        return JsonResponse({'message': message})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)



