from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'catalog.views.index_view'),
    url(r'^admin/settings/', 'my_admin.views.admin_settings'),
    url(r'^admin/', include('my_admin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^login/', 'account.views.login_view'),
    url(r'^registration/', 'account.views.registration_view'),
    url(r'^logout/', 'account.views.logout_view'),
    url(r'^email_confirmation/', 'account.views.email_confirmation_view'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^search/', 'catalog.views.search_view'),
    url(r'', include('pages.urls')),
]
