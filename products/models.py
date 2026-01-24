from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


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
            self.slug = slugify(self.name)
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
            self.slug = slugify(self.name)
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
    sku = models.CharField(_("SKU"), max_length=15, unique=True, choices=FLAG_TYPES)
    description = models.TextField(_("description"), blank=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    flag = models.CharField(_("flag"), max_length=50, blank=True)
    available = models.BooleanField(_("available"), default=True)
    created = models.DateTimeField(_("created"), default=timezone.now)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    image = models.ImageField(_("image"), upload_to='products/', blank=True, null=True)
    slug = models.SlugField(_("slug"), max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
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
    user_name = models.CharField(_("user name"), max_length=100)
    rating = models.PositiveIntegerField(_("rating"), validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(_("Review"), blank=True)
    created = models.DateTimeField(_("created"), default=timezone.now)

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ['-created']

    def __str__(self):
        return f"Review by {self.user_name} for {self.product.name}"