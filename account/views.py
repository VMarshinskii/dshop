# _*_ coding: utf-8 _*_
from django.shortcuts import render_to_response, HttpResponse, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from models import User, EmailConfirmation
from forms import RegistrationForm, AddFunForm
from additions import get_email_provider
from dshop.additions import translit, random_str
from django.utils.translation import ugettext_lazy as _


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


def registration_view(request):
    args = {'form': RegistrationForm()}
    args.update(csrf(request))
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            password = request.POST.get('password')
            new_user.username = translit(request.POST.get('first_name')) + "_" + random_str(10)
            new_user.set_password(password)
            new_user.is_active = False
            new_user.save()

            email_confirmation = EmailConfirmation(user=new_user)
            email_confirmation.save()

            t = get_template('email_confirmation.html')
            html = t.render(Context({
                'user': new_user,
                'password': password,
                'email_confirmation': email_confirmation
            }))
            new_user.email_user(u"Подтверждение email", html)

            email_provider = get_email_provider(new_user.email.split("@")[1])
            return render_to_response('registration_thank', {
                'email_provider_title': _(email_provider[0]),
                'email_provider_url': _(email_provider[1])
            })
        args['form'] = form

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
