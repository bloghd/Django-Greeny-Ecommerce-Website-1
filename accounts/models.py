
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from settings.models import Country, City
from django.db.models.signals import post_save
from django.dispatch import receiver
import random

def generaste_code(length=6):
    nums = '0123456789'
    return ''.join(random.choice(nums) for _ in range(length))


class Profile(models.Model):
    code = models.CharField(_("code"), max_length=15, unique=True, default=generaste_code)
    code_used = models.BooleanField(_("code used"),default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_("user"))
    # bio = models.TextField(_("bio"), blank=True, null=True)
    # birth_date = models.DateField(_("birth date"), blank=True, null=True)
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='user_country', verbose_name=_("country"), null=True)
    # city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='user_city', verbose_name=_("city"), null=True)
    profile_image = models.ImageField(_("profile image"), upload_to='profiles/', blank=True, null=True)
    # phone_number = models.CharField(_("phone number"), max_length=20, blank=True, null=True)
    # address = models.CharField(_("address"), max_length=255, blank=True, null=True)
    # website = models.URLField(_("website"), blank=True, null=True)
    # social_links = models.JSONField(_("social links"), blank=True, null=True, help_text=_("A JSON object containing social media links."))


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)




    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f"Profile of {self.user.username}"
    

DATE_TYPES = [
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Office', 'Office'),
    ('Acadmyy', 'Acadmy'),
    ('Other', 'Other'),
]


class UserPhoneNumber(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_phone_numbers', verbose_name=_("user"))
    phone_number = models.CharField(_("phone number"), max_length=20)
    type = models.CharField(_("type"), max_length=20, choices=DATE_TYPES, default='Other')

    class Meta:
        verbose_name = _("user phone number")
        verbose_name_plural = _("user phone numbers")

    def __str__(self):
        return f"{self.phone_number} ({self.type})"
    
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_addresses', verbose_name=_("user"))
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='user_addresses_country', verbose_name=_("country"), null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='user_addresses_city', verbose_name=_("city"), null=True)
    address = models.CharField(_("address"), max_length=255)
    type = models.CharField(_("type"), max_length=20, choices=DATE_TYPES, default='Other')

    class Meta:
        verbose_name = _("user address")
        verbose_name_plural = _("user addresses")

    def __str__(self):
        return f"{self.address} ({self.type})"