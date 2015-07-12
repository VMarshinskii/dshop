# _*_ coding: utf-8 _*_
from models import User


def registration_valid(request):
    errors = {}
    first_name = request.POST['first_name']
    email = request.POST['email']
    password = request.POST['password']
    password_again = request.POST['password_again']

    if first_name == '':
        errors['first_name_error'] = "обязательное поле"
    if email == '':
        errors['email_error'] = "обязательное поле"
    else:
        try:
            user = User.objects.get(email=email)
            errors['email_error'] = "пользователь с таким email уже существует"
        except User.DoesNotExist:
            pass
    if password == '':
        errors['password_error'] = "обязательное поле"
    if password != password_again:
        errors['password_error'] = "пароли не совпадают"

    return errors