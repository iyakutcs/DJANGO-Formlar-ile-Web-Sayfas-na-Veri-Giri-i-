# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:03:47 2025

@author: iyaku
# """

from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.create_userprofile, name='create_userprofile'),
    path('success/', lambda request: render(request, 'users/success.html'), name='success'),
    # Son iki form giriş ve başarılı giriş sayfaları
]


