from django.shortcuts import render
from .models import Home
from products.models import Product, Category, Brand,Review



def home_view(request):
    home_settings = Home.objects.filter(activate=True)
    featured_products = Product.objects.filter(flag='Featured')[:10]
    new_products = Product.objects.filter(flag='New')[:10]
    categories = Category.objects.all()[:15]
    brands = Brand.objects.all()[:15]
    recent_reviews = Review.objects.order_by('-created')[:5]

    context = {
        'home_settings': home_settings,
        'featured_products': featured_products,
        'new_products': new_products,
        'categories': categories,
        'brands': brands,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'settings/home.html', context)
