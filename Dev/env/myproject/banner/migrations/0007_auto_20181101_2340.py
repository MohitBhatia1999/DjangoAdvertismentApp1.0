# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0006_auto_20181101_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priceperiod',
            name='booking_price',
        ),
        migrations.AddField(
            model_name='priceperiod',
            name='add_content',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
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
