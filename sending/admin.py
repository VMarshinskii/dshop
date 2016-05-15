# -*- coding: utf-8 -*-
from django.contrib import admin
from sending.models import EmailSender


class EmailSenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date',)
    search_fields = ('title', 'description', 'date',)


admin.site.register(EmailSender, EmailSenderAdmin)
