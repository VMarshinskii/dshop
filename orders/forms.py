# coding=utf-8
from django import forms
from models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'index', 'address']

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        index = cleaned_data.get('index')
        address = cleaned_data.get('address')

        if not first_name or not last_name or not email or not phone or not index or not address:
            raise forms.ValidationError("Заполните все поля")
        return cleaned_data