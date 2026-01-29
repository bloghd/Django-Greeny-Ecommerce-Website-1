from .models import Cart, CartItem


def cart_context_processor(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, cart_status='InProgress')
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.get_total_price() for item in cart_items)
        return {
            'cart': cart,
            'cart_items': cart_items,
            'cart_total_price': total_price,
        }
    return {
        'cart': None,
        'cart_items': [],
        'cart_total_price': 0,
    }