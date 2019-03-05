#!/usr/bin/python
# -*-  coding:utf-8  -*-
# @Time   : 2019/3/2  10:57
# @Author : 黄猿
# @File   : urls.py

"""uni_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from reception import views
from django.conf.urls import url


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login, name="reception_login"),
    path('register/', views.register, name="reception_register"),
    path('logout/', views.logout, name="reception_logout"),
    path('article_msg/', views.article_msg, name="get_article_msg"),
    path('check_lift/', views.check_lift),
    path('msg_list/', views.msg_list),
]
