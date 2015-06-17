from django.contrib import admin
from pages.models import Page, Section


# Register your models here.
class AdminPage(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"url": ("title",)}


class AdminSection(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"url": ("title",)}


admin.site.register(Page, AdminPage)
# admin.site.register(Section, AdminSection)