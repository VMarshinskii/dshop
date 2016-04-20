# -*- coding: utf-8 -*-
from django.contrib import admin
from banners.models import RightBanner, Slider
from suit.admin import SortableModelAdmin


class SliderAdmin(SortableModelAdmin):
    sortable = 'order'
    # list_editable = ('title', 'order')


admin.site.register(RightBanner)
admin.site.register(Slider)
#, SliderAdmin