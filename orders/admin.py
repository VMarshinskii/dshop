# coding=utf-8
from django.contrib import admin
from models import Order, DeliveryType, OrderPhone


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('id', 'last_name', 'first_name', 'status', 'date_now')

    fields = ['id', 'user', 'sum', 'status', 'first_name', 'patronymic', 'last_name', 'email', 'phone', 'region',
              'city', 'index', 'address', 'metro', 'delivery', 'delivery_price', 'products', 'admin_comment']



class OrderPhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date')

admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryType)
admin.site.register(OrderPhone, OrderPhoneAdmin)