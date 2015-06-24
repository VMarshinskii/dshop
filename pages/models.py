# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField



class Section(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200)
    keyword = models.CharField("Ключевые слова", max_length=200)
    # text = RedactorField(verbose_name="Текст")
    url = models.CharField("Url", max_length=200)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __unicode__(self):
        return self.title


# класс стриницы
class Page(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=200)
    keyword = models.CharField("Ключевые слова", max_length=200)
    # section = models.ForeignKey(Section, blank=True, default="-1", help_text="Раздел", null=True, verbose_name="Раздел")
    text = RedactorField(verbose_name="Текст", redactor_options={'lang': 'ru', 'buttonSource': 'true'})
    url = models.CharField("Url", max_length=200)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __unicode__(self):
        return self.title