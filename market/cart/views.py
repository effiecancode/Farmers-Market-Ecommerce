from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product

from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

from .models import Cart

@login_required
def add_to_cart(request, product_id):
    # get product instance with given id
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = Cart.objects.get(user=request.user, product=product)
        cart_item.units += 1
        cart_item.save()
        messages.success(request, "Item added to Cart")
    except Cart.DoesNotExist:
        Cart.objects.create(user=request.user, product=product)
        messages.success(request, "Item added to Cart")

    return redirect('product:home')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, 'Item removed from Cart')

    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.units * item.product.unit_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, "cart/cart_detail.html", context)

@login_required
def increment_units(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.units += 1
        cart_item.save()

    return redirect('cart:cart_detail')

@login_required
def decrement_units(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        if cart_item.units > 1:
            cart_item.units -= 1
            cart_item.save()

    return redirect('cart:cart_detail')


# mpesa view
@login_required
def mpesa_pay(request, id):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        cl = MpesaClient()

        try:
            cart_items = Cart.objects.filter(user_id=id)
            total_price = 0

            for cart_item in cart_items:
                total_price += cart_item.total_price

            account_reference = cart_items.first().id
            description = f"{len(cart_items)} items in the cart. Total price: {total_price}."
            callback_url = 'https://api.darajambili.com/express-payment'

            cl.stk_push(phone_number, int(total_price), account_reference, description, callback_url)

            return redirect("cart:cart_detail")
        except Cart.DoesNotExist:
            return HttpResponse("Cart not found")
