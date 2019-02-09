#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:35:46 2019

@author: abhijithneilabraham
"""

from django.urls import path
import views 
urlpatterns=[path('',views.index,name='index'),]