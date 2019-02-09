#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:41:30 2019

@author: abhijithneilabraham
"""

from django.contrib import admin 
from django.urls import include,path
urlpatterns=[
        path('polls/',include('polls.urls')),
        path('admin/',admin.site.urls),]