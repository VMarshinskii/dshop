from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<url>[\-\w]+)', 'pages.views.page_view'),
)
