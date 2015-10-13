#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from tblog.settings import MONGO_POOL

DB = MONGO_POOL.tblog


class IndexView(View):

    def get(self, request):
        self.tpl_name = 'blog/index.html'
        data = DB.blog.find_one()
        return render(request, self.tpl_name, data)
