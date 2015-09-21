# -*- coding: utf-8 -*-
from django.contrib import admin
from catalog.models import Product, Category, Color
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'admin_sort', 'home_status', 'get_str_sort')
    list_filter = ['category', 'home_status']
    search_fields = ['name']
    ordering = ('-get_str_sort',)

    fieldsets = (
        ('Основное', {
            'fields': (
                'name', 'price', 'price_sale', 'category',
                'sale_status', 'count', 'count_status', 'brand',
                'text', 'image', 'images', 'home_status')
        }),
        ('Дополнительные поля', {
            # 'classes': ('collapse',),
            'fields': ('status', 'color', 'size', 'structure', 'related_products')
        }),
        ('SEO', {
            # 'classes': ('collapse',),
            'fields': ('keywords', 'description')
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

    def changelist_view(self, request, extra_context=None):
        list_category = sort_list()
        select_res(list_category)
        vars = {'categories': list_category}
        html = render_to_response('admin/result_content_list.html', vars).content
        mass = {'result_content': html}
        return super(CategoryAdmin, self).changelist_view(request, extra_context=mass)

    def save_model(self, request, obj, form, change):
        if obj.parent is None:
            obj.step = 0
        else:
            obj.step = obj.parent.step + 1
        obj.save()


def sort_list():
    mass_object = []
    roots = Category.objects.filter(parent=None)

    def rec_list(obj):
        obj.title = smart_str("— "*obj.step) + smart_str(obj.title)
        mass_object.append(obj)
        children = Category.objects.filter(parent=obj)

        for child in children:
            rec_list(child)

    for root in roots:
        rec_list(root)

    return mass_object


def select_res(categoryes):
    str_res = ""
    for category in categoryes:
        str_res += smart_str(category.title) + ":" + smart_str(category.id) + ";"
    return str_res

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color)