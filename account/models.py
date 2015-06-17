# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models
# from catalog.models import Video

# Модифицируем поле email.
AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').default = ""
AbstractUser._meta.get_field('first_name').blank = False
AbstractUser._meta.get_field('first_name').default = ""


class User(AbstractUser):
    address = models.TextField("Адрес", blank=True)
    region = models.CharField("Область", max_length=200, blank=True)
    city = models.CharField("Город", max_length=200, blank=True)
    index = models.CharField("Индекс", max_length=200, blank=True)
    phone = models.CharField("Телефон", max_length=200, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
