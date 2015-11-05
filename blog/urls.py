from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.posts_view'),
    url(r'^post/(?P<url>[\-\w]+)/$', 'blog.views.post_view'),
)
