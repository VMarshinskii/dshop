# _*_ coding: utf-8 _*_
from django.shortcuts import render_to_response, HttpResponse
from django.core.context_processors import csrf
from django.contrib import auth
from models import User
from forms import RegistrationForm, AddFunForm
from dshop.additions import random_str, translit
from additions import registration_valid


def login(request):
    args = {}
    if request.GET:
        email = request.GET['email']
        password = request.GET['password']
        try:
            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("true")
            else:
                args['form_error'] = "Данные введены не верно!"
        except User.DoesNotExist:
            args['form_error'] = "Пользователя с таким email не существует!"
    return render_to_response("ajax_login.html", args)


def registration(request):
    args = {'form': RegistrationForm()}
    args.update(csrf(request))
    if request.GET:
        form = RegistrationForm(request.GET)
        password = request.GET['password']
        errors = registration_valid(request)
        if len(errors) == 0:
            new_user = User()
            new_user.first_name = request.GET['first_name']
            new_user.email = request.GET['email']
            new_user.username = translit(new_user.first_name) + "_" + random_str(6)
            new_user.set_password(password)
            new_user.save()
            user = auth.authenticate(username=new_user.username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
            return render_to_response("registration_ready.html")
        else:
            args['form'] = form
            args.update(errors)
    return render_to_response("registration.html", args)


def account_view(request):
    args = {
        'user': request.user,
        'user_active': request.user.is_authenticated(),
    }
    args.update(csrf(request))
    args['error'] = False

    if request.POST:
        user = request.user

        if 'first_name' in request.POST and request.POST.get('first_name', '') != '':
            user.first_name = request.POST['first_name']
        else:
            args['error'] = True
            args['first_name_error'] = "error_field"

        if 'last_name' in request.POST and request.POST.get('last_name', '') != '':
            user.last_name = request.POST['last_name']
        else:
            args['error'] = True
            args['last_name_error'] = "error_field"

        if 'email' in request.POST and request.POST.get('email', '') != '':
            user.email = request.POST['email']
        else:
            args['error'] = True
            args['email_error'] = "error_field"

        if 'phone' in request.POST:
            user.phone = request.POST['phone']

        if args['error'] is False:
            user.save()
            return render_to_response("my_account.html", args)

    return render_to_response("my_account.html", args)


def change_password(request):
    if request.user.is_authenticated() and request.GET:

        old_password = request.GET.get('old_password', '')
        new_password = request.GET.get('new_password', '')

        if new_password == '' :
            return HttpResponse("Новый пароль не может быть пустым")
        elif request.user.check_password(old_password):
            username = request.user.username
            request.user.set_password(new_password)
            request.user.save()
            user = auth.authenticate(username=username, password=new_password)
            if user is not None and user.is_active:
                auth.login(request, user)
            return HttpResponse("Ваш пароль изменён!")
        else:
            return HttpResponse("Старый пароль не верный!")
    else:
        return HttpResponse("Ошибка")


def fun_add_view(request):
    if request.GET:
        form = AddFunForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse("Спасибо! Вы подписаны на наши новости!")
        return HttpResponse("Данные введены не верно!")
    return HttpResponse("false")
