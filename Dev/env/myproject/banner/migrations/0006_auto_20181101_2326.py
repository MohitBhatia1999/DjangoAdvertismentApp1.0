# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0005_auto_20181101_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceperiod',
            name='end_date',
            field=models.DateTimeField(default= '2012-09-04 06:00:00', verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='priceperiod',
            name='start_date',
            field=models.DateTimeField(default= '2012-09-04 06:00:00', verbose_name='start date'),
        ),
    ]
