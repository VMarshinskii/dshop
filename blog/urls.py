from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.posts_view'),
    url(r'^post/(?P<id>\d+)/$', 'blog.views.post_view'),
)
