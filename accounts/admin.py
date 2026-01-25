from django.contrib import admin
from .models import Profile, UserPhoneNumber, UserAddress

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')
    search_fields = ('user__username', 'user__email')

@admin.register(UserPhoneNumber)
class UserPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'type')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('type',)

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'country', 'type')
    search_fields = ('user__username', 'address', 'city__name', 'country__name')
    list_filter = ('type', 'country', 'city')
    
