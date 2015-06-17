# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class RightBanner(models.Model):
    title = models.CharField("Название", max_length=200, blank=True)
    link = models.CharField("Ссылка", max_length=200)
    image = models.ImageField(verbose_name="Изображение", upload_to="static/uploads/")

    class Meta:
        verbose_name_plural = u"Баннеры справа"
        verbose_name = u"Баннер справа"

    def __unicode__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField("Название", max_length=200)
    link = models.CharField("Ссылка", max_length=200)
    image = models.ImageField(verbose_name="Изображение", upload_to="static/uploads/")

    class Meta:
        verbose_name_plural = u"Слайдер"
        verbose_name = u"Слайдер"

    def __unicode__(self):
        return self.title