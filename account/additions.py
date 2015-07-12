# _*_ coding: utf-8 _*_
from models import User


def registration_valid(request):
    errors = {}
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    password_again = request.POST['password_again']

    if first_name == '':
        errors['first_name_error'] = "error_field"
        errors['user_error'] = "- заполните обязательные поля"
    if last_name == '':
        errors['last_name_error'] = "error_field"
        errors['last_name'] = "- заполните обязательные поля"
    if email == '':
        errors['email_error'] = "error_field"
        errors['user_error'] = "- заполните обязательные поля"
    else:
        try:
            user = User.objects.get(email=email)
            errors['user_error'] = "- пользователь с таким email уже существует"
            errors['email_error'] = "error_field"
        except User.DoesNotExist:
            pass
    if password == '':
        errors['password_error'] = "- обязательное поле"
        errors['password_field_error'] = "error_field"
    if password != password_again:
        errors['password_error'] = "- пароли не совпадают"
        errors['password_field_error'] = "error_field"

    return errors