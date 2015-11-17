#!/usr/bin/env python
# encoding: utf-8

from django.views.generic import View
from django.shortcuts import render
from app.articles.models import Article


class IndexView(View):

    def get(self, request):
        self.tpl_name = 'index.html'
        articles = Article.objects.all()
        # TODO limit 10 blog
        return render(request, self.tpl_name, {'articles': articles})
