# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0009_reservation_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date of return'),
        ),
    ]
