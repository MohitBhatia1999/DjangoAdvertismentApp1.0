# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_auto_20181101_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceperiod',
            name='end_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='priceperiod',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date'),
        ),
    ]