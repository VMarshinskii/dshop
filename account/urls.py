from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'account.views.account_view'),
    url(r'^change_password/$', 'account.views.change_password'),
)
