# -*- coding: utf-8 -*-
from django import forms
from models import CartProduct


class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['cart_count', 'cart_size', 'cart_color', 'cart_model']
