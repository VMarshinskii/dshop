from django import template
from my_admin.models import SiteSettings
register = template.Library()

@register.inclusion_tag('templatetags/header.html')
def header_show():
    model = SiteSettings.objects.get(id=1)
    return {'model': model}


@register.inclusion_tag('templatetags/banner_head.html')
def banner_head():
    model = SiteSettings.objects.get(id=1)
    return {'model': model}