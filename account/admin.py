from django.contrib import admin
from account.models import User, Fun


class FunAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(User)
admin.site.register(Fun, FunAdmin)
