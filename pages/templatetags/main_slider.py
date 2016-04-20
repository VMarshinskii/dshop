from django import template
from banners.models import Slider
register = template.Library()

@register.inclusion_tag('templatetags/main_slider.html')
def main_slider():
    sliders = Slider.objects.filter(public=True)
    return {'sliders': sliders}