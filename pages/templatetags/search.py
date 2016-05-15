from django import template
from catalog.models import Category
register = template.Library()


@register.inclusion_tag('templatetags/search.html')
def search():
    return {}