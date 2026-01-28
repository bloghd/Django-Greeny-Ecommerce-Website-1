from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from .models import Order
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def order_list(requset):
    order = Order.objects.filter(user=requset.user)
    return render(requset, 'orders/order_list.html', {'orders': order})