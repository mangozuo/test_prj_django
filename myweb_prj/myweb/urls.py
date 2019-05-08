#!usr/bin/python3
# encoding: utf-8

"""
@author:dell
@file: urls.py
@time: 2019/05/08
"""
app_name = "myweb"

from django.urls import path
from myweb import views_api

urlpatterns = [
    path('get_users/',views_api.get_users,name='get_users'),
]