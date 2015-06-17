# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from catalog.models import Product
from cart.models import CartProduct
from forms import CartProductForm
from additions import get_cart, get_count, get_sum


def cart_index_view(request):
    cart = get_cart(request)
    product_carts = CartProduct.objects.filter(cart=cart)

    for pr in product_carts:
        if pr.sale_status:
            pr.price_sum_new = pr.cart_count * pr.price_sale
        else:
            pr.price_sum_new = pr.cart_count * pr.price

    return render_to_response("cart_index.html", {
        'user': request.user,
        'products': product_carts,
        'sum': get_sum(request),
    })


def add_product_ajax(request):
    if request.GET:
        cart = get_cart(request)
        form = CartProductForm(request.GET)
        cart_product = form.save(commit=False)
        try:
            cart_product.product = Product.objects.get(id=int(request.GET.get('product_id', -1)))
            cart_product.create(cart_product.product)
            cart_product.cart = cart
            cart_product.save()
            return render_to_response("add_in_cart.html", {
                'sum': get_sum(request),
                'count': get_count(request)
            })
        except Product.DoesNotExist:
            pass
    return HttpResponse("Ошибка")


def count_product_ajax(request):
    if request.GET:
        cart_product_id = request.GET.get('product_id', -1)
        count = int(request.GET.get('cart_count', 1))
        try:
            cart_product = CartProduct.objects.get(id=cart_product_id)
            new_count = cart_product.cart_count + count
            cart_product.cart_count = new_count
            cart_product.save()
            if new_count < 1:
                cart_product.delete()
        except CartProduct.DoesNotExist:
            pass

    cart = get_cart(request)
    product_carts = CartProduct.objects.filter(cart=cart)

    for pr in product_carts:
        if pr.sale_status:
            pr.price_sum_new = pr.cart_count * pr.price_sale
        else:
            pr.price_sum_new = pr.cart_count * pr.price

    return render_to_response("cart_ajax.html", {
        'user': request.user,
        'products': product_carts,
        'sum': get_sum(request),
    })


def get_count_cart(request):
    return HttpResponse(get_count(request))

def cart_top_ajax(request):
    count = get_count(request)
    cart_sum = get_sum(request)
    if count == 0:
        return HttpResponse("пусто")
    return HttpResponse(str(count) + " шт. на " + str(cart_sum) + " руб.")