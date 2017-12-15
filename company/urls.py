# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='company'
urlpatterns=[
    url(r'^(?P<index>[0-9]+)$',views.personal_info,name='personal')
]