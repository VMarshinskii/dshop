from django import template
from banners.models import RightBanner
register = template.Library()

@register.inclusion_tag('templatetags/right_banners.html')
def right_banners():
    banners = RightBanner.objects.order_by('?')[:3]
    return {'banners': banners}