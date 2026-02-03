from django.contrib import admin
from django.db.models import Avg
from .models import Category, Brand, Product, ProductImage, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'sku', 'price', 'available', 'created', 'updated', 'review_count', 'average_rating')
    list_filter = ('available', 'created', 'updated', 'category', 'brand')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    search_fields = ('name', 'sku', 'description')
    summernote_fields = '__all__'

    def review_count(self, obj):
        return obj.reviews.count()
    def average_rating(self, obj):
        return obj.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)
    list_filter = ('product',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created')
    search_fields = ('product__name', 'user__username', 'review')
    list_filter = ('rating', 'created')


