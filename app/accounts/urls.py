#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from app.accounts.views import LoginView, RegisterView
from django.contrib import auth

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='account-login'),
    url(r'logout/$', auth.logout, name='account-logout'),
    url(r'register/$', RegisterView.as_view(), name='register'),
]
