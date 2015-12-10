#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url, include
from .index import IndexAdminView

urlpatterns = [
    url(r'^$', IndexAdminView.as_view(), name='admin-index'),
    url(r'articles/', include('mongo_admin.articles.urls')),
]
