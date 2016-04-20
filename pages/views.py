# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from pages.models import Page


# Create your views here.
def page_view(request, url="None"):
    try:
        page = Page.objects.get(url=url)
    except Page.DoesNotExist:
        raise Http404
    return render_to_response("page.html", {
        'user': request.user,
        'page': page
    })

