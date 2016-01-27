#!/usr/bin/env python
# encoding: utf-8

from django.http import Http404
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from mongo_admin.articles.models import Article
from mongoengine.queryset import DoesNotExist, MultipleObjectsReturned


class IndexView(View):

    def get(self, request):
        self.tpl_name = 'index.html'
        articles = Article.objects.all()
        # TODO limit 10 index
        return render(request, self.tpl_name, {'articles': articles})


class IndexDetailView(View):

    def get(self, request, alias_name):
        self.tpl_name = 'articles/detail.html'
        try:
            article = Article.objects.get(alias_name=alias_name)
        except (DoesNotExist, MultipleObjectsReturned):
            raise Http404
        return render(request, self.tpl_name, {'article': article})


class TagView(View):

    def get(self, request, tag_name):
        self.tpl_name = 'index.html'
        articles = Article.objects(tags=tag_name)
        return render(request, self.tpl_name, {'articles': articles})

class CategoryView(View):

    def get(self, request, category_name):
        self.tpl_name = 'index.html'
        articles = Article.objects(categories=category_name)
        return render(request, self.tpl_name, {'articles': articles})



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
