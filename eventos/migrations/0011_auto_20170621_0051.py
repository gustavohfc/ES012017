# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-21 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0010_auto_20170617_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='esporte',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='festa',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='teatro',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
    ]