# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, redirect, Http404
from django.core.context_processors import csrf
from django.contrib import auth
from forms import OrderForm
from dshop.additions import translit, random_str
from models import DeliveryType, Order, OrderPhone
from cart.additions import get_cart, get_sum
from cart.models import CartProduct
from account.models import User


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
        ord.city = request.user.city
        ord.address = request.user.address
        # index
        args['form'] = OrderForm(instance=ord)

    if request.POST:
        if request.POST.get('first_name', "") == "":
            args['user_inform_error'] = True
            args['first_name_error'] = "- обязательное поле"
            is_valid = False
        if request.POST.get('last_name', "") == "":
            args['user_inform_error'] = True
            args['last_name_error'] = "- обязательное поле"
            is_valid = False
        if request.POST.get('email', "") == "":
            args['user_inform_error'] = True
            args['email_error'] = "- обязательное поле"
            is_valid = False
        if request.POST.get('phone', "") == "":
            args['user_inform_error'] = True
            args['phone_error'] = "- обязательное поле"
            is_valid = False

        if request.POST.get('region', "") == "":
            args['address_inform_error'] = True
            args['region_error'] = "- обязательное поле"
            is_valid = False
        if request.POST.get('city', "") == "":
            args['address_inform_error'] = True
            args['city_error'] = "- обязательное поле"
            is_valid = False
        if request.POST.get('index', "") == "":
            args['address_inform_error'] = True
            args['index_error'] = "- обязательное поле"
            is_valid = False
        if request.POST.get('address', "") == "":
            args['address_inform_error'] = True
            args['address_error'] = "- обязательное поле"
            is_valid = False

        if request.POST.get('delivery', "") == "":
            args['delivery_error'] = "- выберите тип доставки"
            is_valid = False

        if 'register' in request.POST:
            password = request.POST.get('password', "")
            password2 = request.POST.get('password2', "")

            if password != "":
                if password != password2:
                    args['password_error'] = "Пароли не совпадают"
                    is_valid = False
            else:
                args['password_error'] = "Введите пароль"
                is_valid = False

            try:
                email = request.POST.get('email', "")
                User.objects.get(email=email)
                args['register_error'] = "Пользователь с таким email уже разегистрирован"
                is_valid = False
            except User.DoesNotExist:
                pass

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
                    order.products.add(pr)
            else:
                args['cart_error'] = "в вашей корзине ничего нет"
            order.save()

            if 'register' in request.POST:
                new_user = User()
                new_user.first_name = request.POST.get('first_name', "")
                new_user.last_name = request.POST.get('last_name', "")
                new_user.email = request.POST.get('email', "")
                new_user.phone = request.POST.get('phone', "")
                new_user.city = request.POST.get('city', "")
                new_user.region = request.POST.get('region', "")
                new_user.index = request.POST.get('index', "")
                new_user.address = request.POST.get('address', "")
                new_user.username = translit(new_user.first_name) + "_" + random_str(6)
                password = random_str(7)
                new_user.set_password(password)
                new_user.save()
                user = auth.authenticate(username=new_user.username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                return redirect("/orders/reg_thanks/")
            elif request.user.is_authenticated():
                request.user.last_name = request.POST.get('last_name', "")
                request.user.phone = request.POST.get('phone', "")
                request.user.city = request.POST.get('city', "")
                request.user.address = request.POST.get('address', "")
                request.user.region = request.POST.get('region', "")
                request.user.index = request.POST.get('index', "")
                request.user.save()

            cart.delete()
            return redirect("/orders/thanks/")

        args['form'] = form
    return render_to_response("create_order.html", args)


def thank_order(request):
    return render_to_response("thank_order.html")

def reg_thank_order(request):
    return render_to_response("thank_register_order.html")


STATUSES = [
    "В обработке",
    "Ждёт оплаты",
]

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
