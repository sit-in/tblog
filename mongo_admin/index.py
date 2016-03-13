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
        self.tpl_name = 'admin/home.html'
        articles = Article.objects.all().order_by('-created_date')
        return render(request, self.tpl_name, {'articles': articles})
