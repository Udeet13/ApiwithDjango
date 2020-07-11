# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:04:28 2020

@author: Lenovo
"""

from django.conf.urls import url 
from signup import views 


urlpatterns = [
        url(r'^api/signup$',views.signup_list),
        ]  
