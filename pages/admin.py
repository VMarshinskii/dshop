from django.contrib import admin
from pages.models import Page, Section
from redactor.fields import RedactorField


# Register your models here.
class AdminPage(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"url": ("title",)}
    widgets = {
        'text': RedactorField(redactor_options={'lang': 'ru', 'buttonSource': 'true'}),
    }


class AdminSection(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"url": ("title",)}


admin.site.register(Page, AdminPage)
# admin.site.register(Section, AdminSection)
