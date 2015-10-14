# _*_ coding: utf-8 _*_
from django import forms
from models import User, Fun


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password_repetition = forms.CharField(max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_repetition = cleaned_data.get('password_repetition')

        if not first_name or not last_name or not email or not password or not password_repetition:
            raise forms.ValidationError("Заполните все поля")
        elif password != password_repetition:
            raise forms.ValidationError("Пароли не совпадают")
        else:
            try:
                User.objects.get(email=email)
                raise forms.ValidationError("Пользователь с таким email уже существует")
            except User.DoesNotExist:
                pass
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'
        self.fields['password_repetition'].label = 'Ещё раз'


class AddFunForm(forms.ModelForm):
    class Meta:
        model = Fun
        fields = ['first_name', 'last_name', 'email']