# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0007_auto_20181101_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceperiod',
            name='price',
            field=models.IntegerField(default=400),
        ),
    ]
