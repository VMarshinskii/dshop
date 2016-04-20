# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0441\u0441\u044b\u043a\u0438')),
                ('description', models.CharField(max_length=100, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('content', redactor.fields.RedactorField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435')),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
        ),
    ]
