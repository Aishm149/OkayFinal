# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_selectchoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='selectChoice',
        ),
        migrations.AddField(
            model_name='post',
            name='selectPrime',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='False'),
        ),
        migrations.AddField(
            model_name='post',
            name='selectStandard',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='False'),
        ),
    ]
