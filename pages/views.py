# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.http import Http404
from pages.models import Page
from catalog.models import Product


def search_view(request):
    q = request.GET.get('q', '')
    for product in Product.search.query(q):
        print product.id
    return HttpResponse("ok")


def page_view(request, url="None"):
    try:
        page = Page.objects.get(url=url)
    except Page.DoesNotExist:
        raise Http404
    return render_to_response("page.html", {
        'user': request.user,
        'page': page
    })

