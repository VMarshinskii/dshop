from django import template
from banners.models import RightBanner
register = template.Library()

@register.inclusion_tag('templatetags/right_banners.html')
def right_banners():
    banners = RightBanner.objects.all().order_by('?')
    return {'banners': banners}