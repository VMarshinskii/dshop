# -*- coding: utf-8 -*-
from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField('Название сайта', max_length=200)
    description = models.CharField('Description', max_length=200)
    keywords = models.CharField('Keywords', max_length=200)

    phone = models.CharField('Телефон', max_length=200)
    email = models.CharField('E-mail', max_length=200)

    vk = models.CharField('Вк', max_length=200)
    inst = models.CharField('Instagram', max_length=200)

    head_banner = models.ImageField("Баннер (главный)", upload_to="static/uploads/", blank=True, max_length=1000)

    def save(self, *args, **kwargs):
        if self.head_banner == '':
            model = SiteSettings.objects.get(id=self.id)
            self.head_banner = model.head_banner
        super(SiteSettings, self).save(*args, **kwargs)