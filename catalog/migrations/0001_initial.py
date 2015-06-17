# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('url', models.CharField(max_length=200, verbose_name=b'Url', blank=True)),
                ('description', models.CharField(max_length=200, verbose_name=b'Description', blank=True)),
                ('keywords', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0', blank=True)),
                ('step', models.IntegerField(verbose_name=b'\xd0\x92\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True)),
                ('parent', models.ForeignKey(default=b'-1', blank=True, to='catalog.Category', null=True, verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0426\u0432\u0435\u0442',
                'verbose_name_plural': '\u0426\u0432\u0435\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('price', models.IntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('price_sale', models.IntegerField(default=0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd1\x81\xd0\xbe \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9')),
                ('sale', models.IntegerField(verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb0, %')),
                ('sale_status', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd1\x83')),
                ('count_status', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7')),
                ('count', models.IntegerField(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80 \xd0\xb2 \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb8')),
                ('status', models.IntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb8', choices=[(0, b'----'), (1, b'\xd0\xa5\xd0\xb8\xd1\x82'), (2, b'\xd0\x9d\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0'), (3, b'\xd0\x90\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'), (4, b'\xd0\xa0\xd0\xb0\xd1\x81\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb6\xd0\xb0'), (5, b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80 \xd0\xb4\xd0\xbd\xd1\x8f'), (6, b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80 \xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb8'), (7, b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80 \xd0\xbc\xd0\xb5\xd1\x81\xd1\x8f\xd1\x86\xd0\xb0')])),
                ('text', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('size', models.CharField(max_length=200, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80', blank=True)),
                ('structure', models.CharField(max_length=200, verbose_name=b'\xd0\xa1\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2', blank=True)),
                ('keywords', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description')),
                ('images', models.TextField(blank=True)),
                ('image', models.CharField(max_length=200, blank=True)),
                ('home_status', models.BooleanField(default=False, verbose_name=b'\xd0\x9d\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9')),
                ('category', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='catalog.Category', null=True)),
                ('color', models.ManyToManyField(to='catalog.Color', max_length=200, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82', blank=True)),
                ('related_products', models.ManyToManyField(related_name='related_products_rel_+', max_length=200, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xbf\xd1\x83\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd1\x83\xd1\x8e\xd1\x89\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd1\x8b', to='catalog.Product', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
    ]
