from django import template
from pages.models import Page
register = template.Library()

@register.inclusion_tag('templatetags/top_menu.html')
def top_menu():
    pages = Page.objects.all()
    return {'pages': pages}