from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from decimal import Decimal
from products.models import Product
import random

def generaste_code(length=6):
    nums = '0123456789'
    return ''.join(random.choice(nums) for _ in range(length))

ORDER_STATUS = [
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    code = models.CharField(_("code"), max_length=15, unique=True, default=generaste_code)
    order_status = models.CharField(_("order status"), max_length=20, choices=ORDER_STATUS, default='Pending')
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
