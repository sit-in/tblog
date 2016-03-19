#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from django.contrib.auth.views import logout
from .views import LoginView, RegisterView

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='account-login'),
    url(r'logout/$', logout,{'next_page': '/'}, name='account-logout'),
    # url(r'register/$', RegisterView.as_view(), name='register'),
]
