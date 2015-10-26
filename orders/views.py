# -*- coding: utf-8 -*-
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render_to_response, HttpResponse, redirect, Http404
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import Context
from django.template.loader import get_template
from forms import OrderForm
from dshop.additions import translit, random_str
from models import DeliveryType, Order, OrderPhone
from cart.additions import get_cart, get_sum
from cart.models import CartProduct
from account.models import User


STATUSES = [
    "В обработке",
    "Ждёт оплаты",
]


def create_order(request):
    args = {
        'form': OrderForm(),
        'delivery_mass': DeliveryType.objects.all(),
        'user': request.user,
        'user_active': request.user.is_authenticated(),
        'cart_sum': get_sum(request),
    }
    args.update(csrf(request))
    is_valid = True

    if request.user.is_authenticated():
        ord = Order()
        ord.first_name = request.user.first_name
        ord.last_name = request.user.last_name
        ord.email = request.user.email
        ord.phone = request.user.phone
        ord.index = request.user.index
        ord.address = request.user.address
        # index
        args['form'] = OrderForm(instance=ord)

    if request.POST:

        if request.POST.get('delivery', "") == "":
            args['delivery_error'] = "- выберите тип доставки"
            is_valid = False

        form = OrderForm(request.POST)
        if is_valid and form.is_valid():
            order = form.save(commit=False)
            delivery = DeliveryType.objects.get(id=request.POST['delivery'])
            order.delivery = delivery.title
            order.delivery_price = delivery.price
            order.status = 0
            if request.user.is_authenticated():
                order.user = request.user
            order.sum = delivery.price + get_sum(request)
            order.save()
            cart = get_cart(request)
            if cart:
                for pr in CartProduct.objects.filter(cart=cart):
                    pr.cart = None
                    pr.save()
                    order.products.add(pr)
            else:
                args['cart_error'] = "в вашей корзине ничего нет"
            order.save()

            if request.user.is_authenticated():
                request.user.first_name = request.POST.get('first_name', "")
                request.user.last_name = request.POST.get('last_name', "")
                request.user.phone = request.POST.get('phone', "")
                request.user.address = request.POST.get('address', "")
                request.user.index = request.POST.get('index', "")
                request.user.save()

            email = request.POST.get('email', "")
            t = get_template('create_order_sender.html')
            html_content = t.render(Context({
                'user_active': request.user.is_authenticated(),
                'order': order,
                'order_status': STATUSES[order.status],
                'products': order.products.all(),
            }))

            msg = EmailMultiAlternatives("Заказ на Darya-Shop", html_content, "daryashop112@gmail.com", [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect("/orders/thanks/")

        args['form'] = form
    return render_to_response("create_order.html", args)


def thank_order(request):
    return render_to_response("thank_order.html", {
        'user_active': request.user.is_authenticated()
    })

def reg_thank_order(request):
    return render_to_response("thank_register_order.html")

def orders_view(request):
    orders = []
    if request.user.is_authenticated():
        for order in Order.objects.filter(user=request.user):
            order.products = order.products.all()
            order.status_name = STATUSES[order.status]
            orders.append(order)

    return render_to_response("orders.html", {
        'orders': orders,
        'user_active': request.user.is_authenticated()
    })

def order_view(request, id=-1):
    try:
        order = Order.objects.get(user=request.user.id, id=id)
        products = []
        for product in order.products.all():
            if product.sale_status:
                product.price_all = product.price_sale * product.cart_count
            else:
                product.price_all = product.price * product.cart_count
            products.append(product)

        return render_to_response("order.html", {
            'order': order,
            'products': products
        })
    except Order.DoesNotExist:
        raise Http404


def create_order_phone(request):
    args = {}
    is_valid = True
    if request.GET:
        if request.GET.get('name', "") == "":
            args['name_error'] = "- обязательное поле"
            is_valid = False
        if request.GET.get('number', "") == "":
            args['number_error'] = "- обязательное поле"
            is_valid = False

        if is_valid:
            name = request.GET.get('name', "")
            number = request.GET.get('number', "")
            phone_order = OrderPhone(name=name, phone=number)
            phone_order.save()
            return render_to_response("create_order_phone_ok.html")

        args['error'] = is_valid

    return render_to_response("create_order_phone.html", args)
