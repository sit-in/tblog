#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View, DetailView
from tblog.settings import MONGO_POOL
from mongo_admin.articles.models import Article
from .forms import ArticleForm

DB = MONGO_POOL.tblog


class ArticlesView(View):

    tpl_name = 'articles/article.html'

    @method_decorator(login_required)
    def post(self, request):
        data = request.POST
        title = data['title']
        content = data['content']
        alias_name = data['alias_name']
        categories = data['categories']
        categories = categories.split(',')
        tags = data['tags']
        tags = tags.split(',')
        author = request.user.id
        form = ArticleForm(data)
        if form.is_valid():
            article = Article(title=title, alias_name=alias_name,
                            content=content, author=author, tags=tags, categories=categories)
            article.save()
        else:
            return render(request, self.tpl_name, {'errors': form.errors.values()[0][0]})
        return HttpResponseRedirect(reverse('admin-index'))

    @method_decorator(login_required)
    def get(self, request):
        articles = Article.objects.all()
        return render(request, self.tpl_name, {'articles': articles})


class ArticlesDetailView(View):
    tpl_name = 'articles/edit.html'

    @method_decorator(login_required)
    def get(self, request, article_id):
        article = Article.objects(id=article_id).first()
        article.tags = ','.join(article.tags)
        article.categories = ','.join(article.categories)
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
        alias_name = data['alias_name']
        cover_pic = data['cover_pic']
        summary = data['summary']
        categories = data['categories']
        categories = categories.split(',')
        tags = data['tags']
        tags = tags.split(',')
        article = Article.objects(id=article_id)
        article.update(title=title,alias_name=alias_name, content=content,
                       tags=tags, categories=categories,cover_pic=cover_pic,
                       summary=summary)
        return HttpResponseRedirect(reverse('articles'))


class ArticlesDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, article_id):
        article = Article.objects(id=article_id)
        article.delete()
        return HttpResponseRedirect(reverse('articles'))
