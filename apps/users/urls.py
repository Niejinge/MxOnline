# _*_ coding: utf-8 _*_
__author__ = 'goldbro'
__date__ = '2018/4/11 20:36'

from django.conf.urls import url, include
from .views import UserinfoView, UploadImageView, UpdatePwdView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # 修改用户密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

]