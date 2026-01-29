from django.urls import path
from .views import register, activate, profile_view, add_wishlist

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('<str:username>/activate/', activate, name='activate'),
    path('profile/', profile_view, name='profile'),
    path('profile/add-wishlist/', add_wishlist, name='add_wishlist'),
]