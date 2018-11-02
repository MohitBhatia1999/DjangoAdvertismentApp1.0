# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import models
from models import *

from django.template import Context, loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



    
def check_availability(request):
	t=0
	for p in PricePeriod.objects.raw('SELECT * from banner_priceperiod'):
		for b in BookingPeriod.objects.raw('SELECT * from banner_bookingperiod'):
				if(  (b.start_date < p.start_date <  b.end_date) or ( b.start_date < p.end_date < b.end_date) ):
					t=1
					return HttpResponse("price change clashes with some booking")
                else:
    				continue
    if(t==0):
    	return HttpResponse("No clashes, you are good to go")
    			