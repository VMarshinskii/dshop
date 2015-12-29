# -*- coding: utf-8 -*-
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db import models
from redactor.fields import RedactorField
from datetime import datetime
from account.models import User, Fun



class Post(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200, blank=True)
    keyword = models.CharField("Ключевые слова", max_length=200, blank=True)
    text = RedactorField(verbose_name="Текст", redactor_options={'upload_to': 'static/uploads'})
    url = models.CharField("Url", max_length=200, unique=True)
    lookbook = models.BooleanField(verbose_name="Публиковать в LookBook", default=False)
    send = models.BooleanField(verbose_name="Разослать подписчикам", default=False)

    lookbook_datetime = models.DateTimeField(verbose_name="Дата публикации", editable=False, null=True)
    send_datetime = models.DateTimeField(verbose_name="Дата рассылки", editable=False, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.lookbook and self.lookbook_datetime is None:
            self.lookbook_datetime = datetime.now()
        if self.send and self.send_datetime is None:
            user_emails = list(User.objects.all().values_list('email', flat=True).distinct())
            print user_emails
            for email in Fun.objects.all().values_list('email', flat=True).distinct():
                if email not in user_emails:
                    user_emails.append(email)
            text = self.text.replace('src="', 'style="width:100%" src="http://darya-shop.ru')
            msg = EmailMultiAlternatives(self.title, text, 'daryashop112@gmail.com', user_emails)
            msg.attach_alternative(text, "text/html")
            msg.send()
            self.send_datetime = datetime.now()
        super(Post, self).save(*args, **kwargs)