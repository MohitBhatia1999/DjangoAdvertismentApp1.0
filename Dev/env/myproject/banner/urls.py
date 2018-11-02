from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'check_availability/$', views.check_availability, name='check_availability'),
]