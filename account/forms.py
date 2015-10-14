# _*_ coding: utf-8 _*_
from django import forms
from models import User, Fun
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label=_(u'Пароль'))
    password_repetition = forms.CharField(max_length=100, widget=forms.PasswordInput(), label=_(u'Ещё раз'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_repetition = cleaned_data.get('password_repetition')

        if not first_name or not last_name or not email or not password or not password_repetition:
            raise forms.ValidationError("Заполните обязательные поля")
        elif password != password_repetition:
            self._errors["password"] = self.error_class(["Введите пароль"])
            self._errors["password_repetition"] = self.error_class(["Повторите пароль"])
            raise forms.ValidationError("Пароли не совпадают")
        else:
            try:
                User.objects.get(email=email)
                raise forms.ValidationError("Пользователь с таким email уже существует")
            except User.DoesNotExist:
                pass
        return cleaned_data


class AddFunForm(forms.ModelForm):
    class Meta:
        model = Fun
        fields = ['first_name', 'last_name', 'email']