# _*_ coding: utf-8 _*_
from django import forms
from models import User, Fun


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']


class AddFunForm(forms.ModelForm):
    class Meta:
        model = Fun
        fields = ['first_name', 'last_name', 'email']