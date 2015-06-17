from django import template
from banners.models import Slider
register = template.Library()

@register.inclusion_tag('templatetags/main_slider.html')
def main_slider():
    sliders = Slider.objects.all()
    return {'sliders': sliders}