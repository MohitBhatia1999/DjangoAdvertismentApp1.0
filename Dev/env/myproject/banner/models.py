# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.core.exceptions import ValidationError

class BookingPeriod(models.Model):
    add_content = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

class PricePeriod(models.Model):
    
    #booking_price = models.IntegerField(default=0)
    #start_date = models.DateTimeField('start date',default='2012-09-04 06:00:00')
    #end_date = models.DateTimeField('end date',default='2012-09-04 06:00:00')
    add_content = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    price = models.IntegerField(default=400)
    



"""
    @classmethod
    def checkbw(self):
		

    	for p in PricePeriod.objects.raw('SELECT * from banner_priceperiod'):
			for b in BookingPeriod.objects.raw('SELECT * from banner_bookingperiod'):
				if(  (b.start_date < p.start_date <  b.end_date) or ( b.start_date < p.end_date < b.end_date) ):
					sraise ValidationError('Start date is after end date')
				else:
					continue

PricePeriod.checkbw()
"""