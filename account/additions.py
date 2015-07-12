# _*_ coding: utf-8 _*_
from models import User


def registration_valid(request):
    errors = {}
    first_name = request.POST['first_name']
    email = request.POST['email']
    password = request.POST['password']
    password_again = request.POST['password_again']

    if first_name == '':
        errors['first_name_error'] = "error_field"
        errors['user_error'] = "Заполните обязательные поля"
    if email == '':
        errors['email_error'] = "error_field"
        errors['user_error'] = "Заполните обязательные поля"
    else:
        try:
            user = User.objects.get(email=email)
            errors['email_error'] = "пользователь с таким email уже существует"
            errors['email_field_error'] = "error_field"
        except User.DoesNotExist:
            pass
    if password == '':
        errors['password_error'] = "Обязательное поле"
        errors['password_field_error'] = "error_field"
    if password != password_again:
        errors['password_error'] = "Пароли не совпадают"
        errors['password_field_error'] = "error_field"

    return errors