# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import BookingPeriod

admin.site.register(BookingPeriod)

from .models import PricePeriod
admin.site.register(PricePeriod)