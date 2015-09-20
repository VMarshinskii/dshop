from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^upload_image/$', 'my_admin.views.video_upload'),
    url(r'^update_product_sort/$', 'my_admin.views.update_product_sort'),
    url(r'^tree_categories/(?P<id>\d+)/', 'my_admin.views.tree_categories'),
    url(r'^get_products_list/', 'my_admin.views.get_products_list'),
)
