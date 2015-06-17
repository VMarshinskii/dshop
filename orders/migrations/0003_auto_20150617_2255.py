# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20150617_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderphone',
            options={'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u0439', 'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0437\u0432\u043e\u043d\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='order',
            name='sum',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0', blank=True),
        ),
    ]
