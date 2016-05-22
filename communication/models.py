# coding=utf-8
from django.db import models
from redactor.fields import RedactorField


class Review(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)
    text = RedactorField(verbose_name="Описание", redactor_options={
        'upload_to': 'static/uploads',
        'clipboardImageUpload ': 'true',
        'multipleImageUpload': 'true'
    }, blank=True)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.datetime)

    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"
