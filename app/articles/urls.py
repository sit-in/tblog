#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from app.articles.views import (
    ArticlesView, ArticlesDetailView,
    ArticlesDeleteView
)

urlpatterns = [
    url(r'/(?P<article_id>[0-9a-z]+)/delete/$', ArticlesDeleteView.as_view(), name='article-delete'),
    url(r'/(?P<article_id>[0-9a-z]+)/$', ArticlesDetailView.as_view(), name='article-edit'),
    url(r'$', ArticlesView.as_view(), name='articles')
]
