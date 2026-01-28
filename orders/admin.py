from django.contrib import admin
from .models import Order, OrderItem, Cart, CartItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'order_status', 'created_at', 'is_paid')
    list_filter = ('order_status', 'is_paid', 'created_at')
    search_fields = ('code',)
    readonly_fields = ('created_at', 'updated_at', 'delivred_at')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__code', 'product__name')
    ordering = ('-order__created_at',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('code', 'cart_status', 'created_at')
    list_filter = ('cart_status', 'created_at')
    search_fields = ('code',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price')
    search_fields = ('cart__code', 'product__name')
    ordering = ('-cart__created_at',)

    


