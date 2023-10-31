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

    # check if product id in uders cart
    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    if cart_item:
        cart_item.units += 1
        cart_item.save()
        messages.success(request, "Item added to Cart")

    else:
        Cart.objects.create(user=request.user, product=product)
        messages.success(request, "Item added to Cart")

    return redirect('cart:cart_detail')

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
def mpesa_pay(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0114622333'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
    data = request.body

    return HttpResponse('STK push in django')
