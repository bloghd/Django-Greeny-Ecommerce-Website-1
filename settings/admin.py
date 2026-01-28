from django.contrib import admin
from .models import Country, City, Company, Home


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name', 'country__code')
    list_filter = ('country',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone_number', 'email', 'website')
    search_fields = ('name', 'city__name', 'city__country__name')
    list_filter = ('city__country',)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'activate')
    search_fields = ('title',)
    list_filter = ('activate',)

    


