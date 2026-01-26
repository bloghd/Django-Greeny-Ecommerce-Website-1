from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(_("country name"), max_length=100, unique=True)
    code = models.CharField(_("country code"), max_length=10, unique=True)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")
        ordering = ['name']

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(_("city name"), max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name=_("country"))

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")
        ordering = ['name']
        unique_together = ('name', 'country')

    def __str__(self):
        return f"{self.name}, {self.country.code}"
    

class Company(models.Model):
    name = models.CharField(_("company name"), max_length=200, unique=True)
    logo = models.ImageField(_("logo"), upload_to='company_logos/', blank=True, null=True)
    description = models.TextField(_("description"), blank=True, null=True)
    address = models.TextField(_("address"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='companies', verbose_name=_("city"))
    phone_number = models.CharField(_("phone number"), max_length=20, blank=True, null=True)
    email = models.EmailField(_("email"), blank=True, null=True)
    website = models.URLField(_("website"), blank=True, null=True)
    facebook_link = models.URLField(_("facebook_link"), blank=True, null=True)
    twitter_link = models.URLField(_("twitter_link"), blank=True, null=True)
    linkedin_link = models.URLField(_("linkedin_link"), blank=True, null=True)
    instagram_link = models.URLField(_("instagram_link"), blank=True, null=True)


    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companies")
        ordering = ['name']

    def __str__(self):
        return self.name
    

