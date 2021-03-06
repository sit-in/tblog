#!/usr/bin/env python
# encoding: utf-8

from __future__ import division

import math
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from mongo_admin.articles.models import Article
from mongoengine.queryset import DoesNotExist, MultipleObjectsReturned
from markdown import markdown
from markdown.extensions import codehilite, extra

PER_PAGE_ARTICLE_NUM = 6


class IndexView(View):

    def get(self, request, *args, **kwargs):
        tpl_name = 'index.html'
        total_article_num = len(Article.objects)
        total_page = int(math.ceil(total_article_num/PER_PAGE_ARTICLE_NUM))
        articles = Article.objects[0:PER_PAGE_ARTICLE_NUM].order_by('-created_date')
        page_num = 1
        ret = {
            'articles': articles,
            'total_page': total_page,
            'page_num': page_num,
        }
        return render(request, tpl_name, ret)


class IndexDetailView(View):

    def get(self, request, alias_name):
        tpl_name = 'articles/detail.html'
        try:
            article = Article.objects.get(alias_name=alias_name)
            article.content = markdown(article.content,
                                       extensions=[extra.ExtraExtension(),
                                                   codehilite.CodeHiliteExtension()])
        except (DoesNotExist, MultipleObjectsReturned):
            raise Http404
        return render(request, tpl_name, {'article': article})


class TagView(View):

    def get(self, request, tag_name, page_num=1):
        tpl_name = 'index.html'
        articles = Article.objects(tags=tag_name)
        total_article_num = len(articles)
        total_page = int(math.ceil(total_article_num/PER_PAGE_ARTICLE_NUM))
        articles = articles[0:PER_PAGE_ARTICLE_NUM].order_by('-created_date')
        ret = {
            'articles': articles,
            'total_page': total_page,
            'page_num': page_num,
        }
        return render(request, tpl_name, ret)


class CategoryView(View):

    def get(self, request, category_name, page_num=1):
        tpl_name = 'index.html'
        articles = Article.objects(categories=category_name)
        total_article_num = len(articles)
        total_page = int(math.ceil(total_article_num/PER_PAGE_ARTICLE_NUM))
        articles = articles[0:PER_PAGE_ARTICLE_NUM].order_by('-created_date')
        ret = {
            'articles': articles,
            'total_page': total_page,
            'page_num': page_num,
        }
        return render(request, tpl_name, ret)


class PageView(View):

    def get(self, request, page_num):
        tpl_name = 'index.html'
        try:
            page_num = int(page_num)
        except:
            page_num = 1
        if page_num == 1:
            return HttpResponseRedirect(reverse('index'))
        total_article_num = len(Article.objects)
        total_page = int(math.ceil(total_article_num/PER_PAGE_ARTICLE_NUM))
        articles = Article.objects[PER_PAGE_ARTICLE_NUM*(page_num-1):page_num*PER_PAGE_ARTICLE_NUM]
        ret = {
            'articles': articles,
            'total_page': total_page,
            'page_num': page_num,
        }
        return render(request, tpl_name, ret)


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
