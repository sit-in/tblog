#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from tblog.settings import MONGO_POOL
from app.articles.models import Article
from bson.objectid import ObjectId

DB = MONGO_POOL.tblog


class ArticlesView(View):

    def post(self, request):
        data = request.POST
        title = data['title']
        content = data['content']
        tags = data['tags']
        tags = tags.split(',')
        # author = request.user.id
        author = ObjectId()
        article = Article(title=title, content=content, author=author, tags=tags)
        article.save()
        return HttpResponseRedirect(reverse('articles'))

    def get(self, request):
        self.tpl_name = 'articles/article.html'
        articles = Article.objects.all()
        # TODO limit 10 blog
        return render(request, self.tpl_name, {'articles': articles})


class ArticlesDetailView(View):

    def get(self, request, article_id):
        self.tpl_name = 'articles/detail.html'
        article = Article.objects(id=article_id).first()
        data = {
            'article': article,
            'article_id': article_id
            }
        return render(request, self.tpl_name, data)

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
    def get(self, request, article_id):
        article = Article.objects(id=article_id)
        article.delete()
        return HttpResponseRedirect(reverse('articles'))
