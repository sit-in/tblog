#!/usr/bin/env python
# encoding: utf-8

from django.views.generic import View
from django.shortcuts import render
from mongo_admin.articles.models import Article


class IndexView(View):

    def get(self, request):
        self.tpl_name = 'index.html'
        articles = Article.objects.all()
        # TODO limit 10 index
        return render(request, self.tpl_name, {'articles': articles})


class IndexDetailView(View):

    def get(self, request, alias_name):
        self.tpl_name = 'articles/detail.html'
        article = Article.objects.get(alias_name=alias_name)
        return render(request, self.tpl_name, {'article': article})
