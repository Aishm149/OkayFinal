# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-11 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170310_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='selectPrime',
        ),
        migrations.RemoveField(
            model_name='post',
            name='selectStandard',
        ),
    ]
