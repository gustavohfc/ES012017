# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-23 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170423_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='user_type',
            field=models.CharField(choices=[('US', 'Usuario comum'), ('PR', 'Promovedor de enventos')], default='US', max_length=2),
        ),
    ]