#!/usr/bin/env python
# encoding: utf-8


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render
from mongo_admin.articles.models import Article


class IndexAdminView(View):

    @method_decorator(login_required)
    def get(self, request):
        self.tpl_name = 'admin_index.html'
        articles = Article.objects.all()
        return render(request, self.tpl_name, {'articles': articles})