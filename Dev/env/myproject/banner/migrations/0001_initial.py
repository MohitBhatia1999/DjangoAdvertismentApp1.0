# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_content', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
            ],
        ),
        migrations.CreateModel(
            name='PricePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_price', models.IntegerField(default=0)),
                ('bookingperiod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banner.BookingPeriod')),
            ],
        ),
    ]
