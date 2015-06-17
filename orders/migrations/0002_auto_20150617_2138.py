# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('phone', models.CharField(max_length=250, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0437\u0432\u043e\u043d\u043a\u0438',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u0439',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='cart.CartProduct', verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0', choices=[(0, b'\xd0\x92 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb5'), (1, b'\xd0\x96\xd0\xb4\xd1\x91\xd1\x82 \xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8b')]),
        ),
    ]
