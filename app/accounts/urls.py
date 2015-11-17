#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from app.accounts.views import LoginView, RegisterView

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'register/$', RegisterView.as_view(), name='register'),
]
