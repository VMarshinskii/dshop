from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'cart.views.cart_index_view'),
    url(r'^add_in_cart/$', 'cart.views.add_product_ajax'),
    url(r'^change_count_product/$', 'cart.views.count_product_ajax'),
    url(r'^get_count_cart/$', 'cart.views.get_count_cart'),
    url(r'^cart_top_ajax/$', 'cart.views.cart_top_ajax'),
)
