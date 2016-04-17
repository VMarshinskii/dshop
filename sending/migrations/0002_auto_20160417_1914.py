# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsender',
            name='description',
            field=models.CharField(max_length=100, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
