from django import template
from catalog.models import Category
register = template.Library()

@register.inclusion_tag('templatetags/catalog_menu.html')
def catalog_menu(active_categ=None):
    parents = Category.objects.filter(parent=None, public=True)
    mass_categ = {}
    for parent in parents:
        if active_categ and parent.id == active_categ.id:
            parent.active = True
        mass_categories = []
        childrens = Category.objects.filter(parent=parent, public=True)
        for child in childrens:
            mass_categories.append(child)
        mass_categ[parent] = mass_categories
    return {'mass_categ': mass_categ}