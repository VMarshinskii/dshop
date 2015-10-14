# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models
# from catalog.models import Video

# Модифицируем поле email.
from dshop.additions import random_str

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').default = ""
AbstractUser._meta.get_field('email').verbose_name = "E-mail"
AbstractUser._meta.get_field('first_name').blank = False
AbstractUser._meta.get_field('first_name').default = ""
AbstractUser._meta.get_field('last_name').blank = False
AbstractUser._meta.get_field('last_name').default = ""


class User(AbstractUser):
    address = models.TextField("Адрес", blank=True)
    region = models.CharField("Область", max_length=200, blank=True)
    city = models.CharField("Город", max_length=200, blank=True)
    index = models.CharField("Индекс", max_length=200, blank=True)
    phone = models.CharField("Телефон", max_length=200, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Fun(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=250)
    last_name = models.CharField(verbose_name="Фамилия", max_length=250, blank=True)
    email = models.CharField(verbose_name="E-mail", max_length=250, unique=True)
    phone = models.CharField(verbose_name="Телефон", max_length=250, blank=True)
    date_create = models.DateTimeField(verbose_name="Дата подписки", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    def __unicode__(self):
        return self.first_name + u" : " + self.email


class EmailConfirmation(models.Model):
    user = models.ForeignKey(User, verbose_name="user")
    hash = models.CharField(verbose_name="Хеш", max_length=200, default='')

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = random_str(20)
        super(EmailConfirmation, self).save(*args, **kwargs)