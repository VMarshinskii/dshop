# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponse
from catalog.additions import sorted_product
from catalog.models import Product, Category, ProductVideo
from banners.models import Slider

sticker = ['нет', 'Хит', 'Новинка', 'Акция', 'Распродажа', 'Товар дня', 'Товар недели', 'Товар месяца', 'Хит сезона']


def index_view(request):
    products = []

    for slider in Slider.objects.filter(public=True):
        slider.order = slider.id
        slider.save()

    # строка "category__public=True" отключает возможность отобразить товар неотображаемой категории (не сезон)
    for product in reversed(Product.objects.filter(public=True, home_status=True, category__public=True).order_by('sort')):
        # не даёт возможности отобразить товар отключённой категории (включая отключённые родительские категории)
        if product.category.public_check():
            product.sticker = sticker[int(product.status)]
            products.append(product)

    sort = request.COOKIES.get('sort', 'default')
    if sort:
        products = sorted_product(products, sort)

    return render_to_response("index.html", {
        'user': request.user,
        'products': products,
        'sort_option': sort
    })


def product_view(request, id=-1):
    if id != -1:
        product = Product.objects.get(public=True, category__public=True, id=id)

        # при попытке отобразить страницу непубликуемого товара или товара непубликуемой категории/подкатегории
        if product.category.public_check():
            return Http404

        images = []
        images_mass = product.images.split(";")
        for img in images_mass:
            if img != '' and img != product.image:
                images.append(img)

        sizes = []
        for size in product.size.split(","):
            if size != '':
                sizes.append(size)

        product.popularity += 1
        product.save()

        return render_to_response("product.html", {
            'user': request.user,
            'product': product,
            'images': images,
            'related_products': product.related_products.all(),
            'sticker': sticker[int(product.status)],
            'sizes': sizes,
            'colors': product.color.all(),
            'models': product.model.all(),
            'path': list(reversed(product.category.get_path_categ())),
            'videos': ProductVideo.objects.filter(product=product)
        })
    else:
        return Http404


def category_view(request, url="none"):
    try:
        categ = Category.objects.filter(public=True).get(url=url)
        products = []

        for product in categ.get_all_product():
            if product.public:
                product.sticker = sticker[int(product.status)]
                products.append(product)

        sort = request.COOKIES.get('sort', 'default')
        if sort:
            products = sorted_product(products, sort)

        path = list(reversed(categ.get_path_categ()))
    except Category.DoesNotExist:
        return Http404
    return render_to_response("category.html", {
        'user': request.user,
        'path': path,
        'categ': categ,
        'products': products,
        'sort_option': sort,
        'children': Category.objects.filter(public=True, parent=categ)
    })


def update_sort_products(request):
    for product in Product.objects.all():
        product.save()
    return HttpResponse("ok")


def search_view(request):
    q = request.GET.get('q', '')
    sort = request.COOKIES.get('sort', 'default')

    prs = []

    for pr in Product.search.query(q):
        if pr.public:
            pr.sticker = sticker[int(pr.status)]
            prs.append(pr)

    return render_to_response("search.html", {
        'user': request.user,
        'q': q,
        'products': Product.search.query(q),
        'sort_option': sort
    })

