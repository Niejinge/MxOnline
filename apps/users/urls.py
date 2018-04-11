# _*_ coding: utf-8 _*_
__author__ = 'goldbro'
__date__ = '2018/4/11 20:36'

from django.conf.urls import url, include
from .views import UserinfoView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),
]