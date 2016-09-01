# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.db import models
from redactor.fields import RedactorField
from account.models import Fun
import threading


class EmailSender(models.Model):
    title = models.CharField(u'Название рассыки', max_length=100)
    description = models.CharField(u'Описание', max_length=100, blank=True)
    content = RedactorField(verbose_name=u'Содержимое')
    date = models.DateField(u'Дата создания', auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.description)

    def save(self, *args, **kwargs):
        # SenderThread(self).start()

        text = unicode(self.content.replace('src="', 'style="width:100%" src="http://darya-shop.ru'))
        msg = EmailMultiAlternatives(unicode(self.title), text, 'DaryaShop <daryashop112@gmail.com>', ['marshinskii@gmail.com'])
        msg.attach_alternative(text, "text/html")
        msg.send()

        super(EmailSender, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Рассылки"
        verbose_name = "Рассылка"


class SenderThread(threading.Thread):
    def __init__(self, param):
        threading.Thread.__init__(self)
        self.daemon = True
        self.param = param

    def run(self):
        user_emails = list(Fun.objects.all().values_list('email', flat=True).distinct())
        text = unicode(self.param.content.replace('src="', 'style="width:100%" src="http://darya-shop.ru'))
        msg = EmailMultiAlternatives(unicode(self.param.title), text, 'daryashop112@gmail.com', user_emails)
        msg.attach_alternative(text, "text/html")
        msg.send()
