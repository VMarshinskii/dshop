# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(max_length=200, verbose_name=b'\xd0\xa5\xd0\xb5\xd1\x88')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('price', models.CharField(max_length=200, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0', blank=True)),
                ('price_sale', models.CharField(max_length=200, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd1\x81\xd0\xbe\xd1\x81 \xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9', blank=True)),
                ('sale_status', models.CharField(max_length=200, verbose_name=b'\xd0\xa1\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd1\x83', blank=True)),
                ('image', models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('cart_count', models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', blank=True)),
                ('cart_size', models.CharField(max_length=200, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80', blank=True)),
                ('cart_color', models.CharField(max_length=200, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82', blank=True)),
                ('cart_price', models.IntegerField(default=0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xb8 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb5')),
                ('cart', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb0', to='cart.Cart', null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', to='catalog.Product', null=True)),
            ],
        ),
    ]
