from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from .models import Order, Cart, CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def order_list(requset):
    order = Order.objects.filter(user=requset.user)
    return render(requset, 'orders/order_list.html', {'orders': order})


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        product = get_object_or_404(Product, id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user, cart_status='InProgress')

        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={
            'price': product.price,
            'quantity': quantity,
            'total': product.price * quantity
        })

        if not item_created:
            cart_item.quantity += quantity
            cart_item.total = cart_item.get_total_price()
            cart_item.save()

        return JsonResponse({'message': 'Product added to cart successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)