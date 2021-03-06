# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, verbose_name='login')),
                ('first_name', models.CharField(max_length=200, verbose_name='first name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last name')),
                ('phone', models.CharField(max_length=20, verbose_name='phone number')),
                ('email', models.CharField(max_length=100, verbose_name='e-mail')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_info', models.CharField(max_length=200, verbose_name='good info')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Customer')),
            ],
        ),
    ]
