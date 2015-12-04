#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from tblog.settings import MONGO_POOL
from mongo_admin.articles.models import Article

DB = MONGO_POOL.tblog


class ArticlesView(View):

    @method_decorator(login_required)
    def post(self, request):
        data = request.POST
        title = data['title']
        content = data['content']
        alias_name = data['alias_name']
        tags = data['tags']
        tags = tags.split(',')
        author = request.user.id
        article = Article(title=title, alias_name=alias_name,
                        content=content, author=author, tags=tags)
        article.save()
        return HttpResponseRedirect(reverse('articles'))

    @method_decorator(login_required)
    def get(self, request):
        self.tpl_name = 'articles/article.html'
        articles = Article.objects.all()
        # TODO limit 10 blog
        return render(request, self.tpl_name, {'articles': articles})


class ArticlesDetailView(View):

    @method_decorator(login_required)
    def get(self, request, article_id):
        self.tpl_name = 'articles/edit.html'
        article = Article.objects(id=article_id).first()
        data = {
            'article': article,
            'article_id': article_id
            }
        return render(request, self.tpl_name, data)

    @method_decorator(login_required)
    def post(self, request, article_id):
        data = request.POST
        title = data['title']
        content = data['content']
        tags = data['tags']
        tags = tags.split(',')
        article = Article.objects(id=article_id)
        article.update(title=title, content=content, tags=tags)
        return HttpResponseRedirect(reverse('articles'))


class ArticlesDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, article_id):
        article = Article.objects(id=article_id)
        article.delete()
        return HttpResponseRedirect(reverse('articles'))
