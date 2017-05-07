# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-07 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20170423_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='authorized_promoter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_type',
            field=models.CharField(choices=[('US', 'Usuario comum'), ('PR', 'Promoter')], default='US', max_length=2),
        ),
    ]