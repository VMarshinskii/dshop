# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb0')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description')),
                ('keywords', models.CharField(max_length=200, verbose_name=b'Keywords')),
                ('phone', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('email', models.CharField(max_length=200, verbose_name=b'E-mail')),
                ('vk', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xba')),
                ('inst', models.CharField(max_length=200, verbose_name=b'Instagram')),
                ('head_banner', models.ImageField(upload_to=b'static/uploads/', max_length=1000, verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xb5\xd1\x80 (\xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9)', blank=True)),
            ],
        ),
    ]
