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
    

