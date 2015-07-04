from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', 'blog.views.posts_view'),
    url(r'^(?P<url>[\-\w]+)/', 'pages.views.page_view'),
)
