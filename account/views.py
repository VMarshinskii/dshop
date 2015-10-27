# _*_ coding: utf-8 _*_
from django.http import Http404
from django.shortcuts import render_to_response, HttpResponse, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from models import User, EmailConfirmation
from forms import RegistrationForm, AddFunForm, LoginForm
from additions import get_email_provider
from dshop.additions import translit, random_str
from django.utils.translation import ugettext_lazy as _


def login_view(request):
    args = {
        'user': request.user,
        'form': LoginForm()
    }
    if request.GET:
        form = LoginForm(request.GET)
        if form.is_valid():
            email = request.GET['login']
            password = request.GET['password']
            next_page = request.GET.get('next', '')
            try:
                user = User.objects.get(email=email)
                user = auth.authenticate(username=user.username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    if next_page:
                        return redirect(next_page)
                    return redirect('/')
            except User.DoesNotExist:
                args['form_error'] = "Пользователя с таким email не существует!"
        args['form'] = form
        args['next_page'] = request.GET.get('next', '')
    return render_to_response("login.html", args)


def logout_view(request):
    auth.logout(request)
    return redirect("/")


def registration_view(request):
    args = {
        'form': RegistrationForm(),
        'user': request.user,
    }
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

            email_confirmation = EmailConfirmation(user=new_user, ps=password)
            email_confirmation.save()

            t = get_template('send_email_confirmation.html')
            html = t.render(Context({
                'user': new_user,
                'password': password,
                'email_confirmation': email_confirmation
            }))
            new_user.email_user(u"Подтверждение email", html)

            args = {}
            email_provider = get_email_provider(new_user.email.split("@")[1])
            if email_provider:
                args = {
                    'email_provider_title': _(email_provider[0]),
                    'email_provider_url': _(email_provider[1])
                }
            return render_to_response('registration_thank', args)
        args['form'] = form

    return render_to_response("registration.html", args)


def email_confirmation_view(request):
    confirmation_hash = request.GET.get('hash', '')
    confirmation_id = request.GET.get('i', '-1')
    try:
        email_confirmation = EmailConfirmation.objects.get(id=int(confirmation_id), hash=confirmation_hash)
        email_confirmation.user.is_active = True
        email_confirmation.user.save()
        user = auth.authenticate(username=email_confirmation.user.username, password=email_confirmation.ps)
        auth.login(request, user)
        email_confirmation.delete()
        return render_to_response("email_confirmation.html", {'user': request.user,})
    except EmailConfirmation.DoesNotExist:
        raise Http404


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
