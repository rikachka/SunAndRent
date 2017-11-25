# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0004_good_reservation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='title',
            field=models.CharField(default='without_title', max_length=100, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='good_info',
            field=models.CharField(max_length=1000, verbose_name='good info'),
        ),
    ]
