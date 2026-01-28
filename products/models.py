from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
import random
from django.contrib.auth.models import User

def generaste_code(length=6):
    nums = '0123456789'
    return ''.join(random.choice(nums) for _ in range(length))


class Category(models.Model):
    name = models.CharField(_("name"), max_length=100, unique=True)
    slug = models.SlugField(_("slug"), max_length=100, unique=True, blank=True)
    image = models.ImageField(_("image"), upload_to='categories/', blank=True, null=True)


    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(_("name"), max_length=100, unique=True)
    slug = models.SlugField(_("slug"), max_length=100, unique=True, blank=True)
    image = models.ImageField(_("Image"), upload_to='brands/', blank=True, null=True)

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Brand.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

FLAG_TYPES = [
    ('New', 'New'),
    ('Featured', 'Featured'),
] 
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', verbose_name=_("category"), null=True, )
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='products', verbose_name=_("brand"), null=True, blank=True)
    name = models.CharField(_("name"), max_length=200)
    sku = models.CharField(_("SKU"), max_length=15, default=generaste_code)
    description = models.TextField(_("description"), blank=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    flag = models.CharField(_("flag"), max_length=50, blank=True, choices=FLAG_TYPES)
    available = models.BooleanField(_("available"), default=True)
    created = models.DateTimeField(_("created"), default=timezone.now)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    image = models.ImageField(_("image"), upload_to='products/', blank=True, null=True)
    slug = models.SlugField(_("slug"), max_length=200, unique=True, blank=True)
    stock = models.PositiveIntegerField(_("stock"), default=0)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_("product"))
    image = models.ImageField(_("image"), upload_to='product_images/')

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")

    def __str__(self):
        return f"Image for {self.product.name}"
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name=_("product"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"), related_name='user')
    rating = models.PositiveIntegerField(_("rating"), validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(_("Review"), blank=True)
    created = models.DateTimeField(_("created"), default=timezone.now)

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ['-created']

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"