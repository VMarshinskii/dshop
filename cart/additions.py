# -*- coding: utf-8 -*-
from models import Cart, CartProduct
from dshop.additions import random_str


def get_cart(request):
    if 'cart_hash' in request.session:
        cart_hash = request.session['cart_hash']
        try:
            return Cart.objects.get(hash=cart_hash)
        except Cart.DoesNotExist:
            pass
    cart = Cart()
    cart.hash = random_str(25)
    cart.save()
    request.session['cart_hash'] = cart.hash
    return cart


def get_sum(request):
    cart = get_cart(request)
    products = CartProduct.objects.filter(cart=cart)
    summa = 0
    for product in products:
        if product.sale_status:
            summa += product.price_sale * product.cart_count
        else:
            summa += product.price * product.cart_count
    return summa


def get_count(request):
    cart = get_cart(request)
    products = CartProduct.objects.filter(cart=cart)
    count = 0
    for product in products:
        count += product.cart_count
    return count
