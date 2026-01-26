from .models import Product, Category, Brand

def products_context_processors(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    category_with_products = []
    for category in categories:
        products = Product.objects.filter(category=category)[:5]
        category_with_products.append({
            'category': category,
            'products': products
        })

    brand_with_products = []
    for brand in brands:
        products = Product.objects.filter(brand=brand)[:5]
        brand_with_products.append({
            'brand': brand,
            'products': products
        })

    return {
        'categories': categories,
        'brands': brands,
        'category_with_products': category_with_products,
        'brand_with_products': brand_with_products,
    }
