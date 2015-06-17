from django import template
from catalog.models import Category
register = template.Library()

@register.inclusion_tag('templatetags/catalog_menu.html')
def catalog_menu():
    parents = Category.objects.filter(parent=None)
    mass_categ = {}
    for parent in parents:
        mass_categories = []
        childrens = Category.objects.filter(parent=parent)
        for child in childrens:
            mass_categories.append(child)
        mass_categ[parent] = mass_categories
    return {'mass_categ': mass_categ}