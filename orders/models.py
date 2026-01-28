from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from decimal import Decimal
from products.models import Product
from django.contrib.auth.models import User
import random

def generaste_code(length=6):
    nums = '0123456789'
    return ''.join(random.choice(nums) for _ in range(length))



CART_STATUS = [
    ('InProgress', 'InProgress'),
    ('Completed', 'Completed'),

]

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart', verbose_name=_("user"))
    code = models.CharField(_("code"), max_length=15, unique=True, default=generaste_code)
    cart_status = models.CharField(_("cart status"), max_length=20, choices=CART_STATUS, default='InProgress')
    created_at = models.DateTimeField(_("created at"), default=timezone.now)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    delivred_at = models.DateTimeField(_("delivred at"), null=True, blank=True)
    is_paid = models.BooleanField(_("is paid"), default=False)

    class Meta:
        verbose_name = _("cart")
        verbose_name_plural = _("carts")
        ordering = ['-created_at']

    def __str__(self):
        return f"Cart {self.code} - {self.cart_status}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name=_("cart"))
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_items', verbose_name=_("product"))
    quantity = models.PositiveIntegerField(_("quantity"), default=1)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = _("cart item")
        verbose_name_plural = _("cart items")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.code}"
    def get_total_price(self):
        return self.quantity * self.price
  

ORDER_STATUS = [
    ('Recieved', 'Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders', verbose_name=_("user"))
    code = models.CharField(_("code"), max_length=15, unique=True, default=generaste_code)
    order_status = models.CharField(_("order status"), max_length=20, choices=ORDER_STATUS, default='Recieved')
    created_at = models.DateTimeField(_("created at"), default=timezone.now)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    delivred_at = models.DateTimeField(_("delivred at"), null=True, blank=True)
    is_paid = models.BooleanField(_("is paid"), default=False)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.code} - {self.order_status}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_("order"))
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items', verbose_name=_("product"))
    quantity = models.PositiveIntegerField(_("quantity"), default=1)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.code}"
    def get_total_price(self):
        return self.quantity * self.price
    
    
