# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-07 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0010_auto_20190507_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='cargadas',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
