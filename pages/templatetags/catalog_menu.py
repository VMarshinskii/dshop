from django import template
from catalog.models import Category
register = template.Library()


@register.inclusion_tag('templatetags/catalog_menu.html')
def catalog_menu(active_categ=None):
    parents = Category.objects.filter(parent=None, public=True).order_by('sort')
    mass_parents = []
    for parent in parents:
        if active_categ and parent.id == active_categ.id:
            parent.active = True
            mass_parents.append(parent)
    return {'mass_parents': mass_parents}