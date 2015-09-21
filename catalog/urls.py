from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'catalog.views.index_view'),
    url(r'^update_sort_products/$', 'catalog.views.update_sort_products'),
    url(r'^product/(?P<id>\d+)/$', 'catalog.views.product_view'),
    url(r'^(?P<url>[\-\w]+)/$', 'catalog.views.category_view')
)
