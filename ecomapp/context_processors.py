from .models import *


def my_context_processor(request):
    # Define your context variables here

    header_categories = Category.objects.all()

    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None
    all_view = {
        'cart': cart,
        'header_categories':header_categories
    }

    return all_view