from django.contrib import admin
from models import Order, DeliveryType, OrderPhone


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'status', 'date_now')


class OrderPhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date')

admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryType)
admin.site.register(OrderPhone, OrderPhoneAdmin)