from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'orders.views.orders_view'),
    url(r'^view/(?P<id>\d+)/$', 'orders.views.order_view'),
    url(r'^create/$', 'orders.views.create_order'),
    url(r'^thanks/$', 'orders.views.thank_order'),
    url(r'^reg_thanks/$', 'orders.views.reg_thank_order'),
    url(r'^create_order_phone/$', 'orders.views.create_order_phone'),
)
