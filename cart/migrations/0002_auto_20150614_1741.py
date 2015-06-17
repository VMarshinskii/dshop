# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='price',
            field=models.IntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='price_sale',
            field=models.IntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd1\x81\xd0\xbe\xd1\x81 \xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='sale_status',
            field=models.BooleanField(verbose_name=b'\xd0\xa1\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd1\x83'),
        ),
    ]
