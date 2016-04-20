# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='text',
            field=redactor.fields.RedactorField(default=b'30', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
            preserve_default=False,
        ),
    ]
