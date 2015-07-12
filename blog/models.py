# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField



class Post(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200, blank=True)
    keyword = models.CharField("Ключевые слова", max_length=200, blank=True)
    text = RedactorField(verbose_name="Текст", redactor_options={'upload_to': 'static/uploads'})
    url = models.CharField("Url", max_length=200, unique=True)
    lookbook = models.BooleanField(verbose_name="Публиковать в LookBook", default=False)
    send = models.BooleanField(verbose_name="Разослать подписчикам", default=False)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __unicode__(self):
        return self.title
