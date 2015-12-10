#!/usr/bin/env python
# encoding: utf-8

from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import BlogUser
from .forms import RegisterForm, LoginForm


class LoginView(View):

    def get(self, request):
        self.tpl_name = 'accounts/login.html'
        return render(request, self.tpl_name)

    def post(self, request):
        self.tpl_name = 'accounts/login.html'
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('articles'))
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            login(request, user)
            return HttpResponseRedirect(reverse('articles'))
        else:
            data = {
                'errors': form.errors.values()[0][0],
                'status': 'error',
            }
        return render(request, self.tpl_name, data)


class RegisterView(View):

    def get(self, request):
        self.tpl_name = 'accounts/register.html'
        return render(request, self.tpl_name, {})

    def post(self, request):
        tpl_name = 'accounts/register.html'
        ret = {}
        redirect_url = reverse('articles')
        request_data = request.POST

        user = BlogUser.objects.filter(username=request_data.get('email'))
        if user:
            ret = {
                'status': 'error',
                'errors': u'当前用户已经存在',
                'data': request.POST
            }
            return render(request, tpl_name, ret)
        form = RegisterForm(request_data)
        if form.is_valid():
            user = form.save(request_data)
            # TODO sendemail
            return HttpResponseRedirect(redirect_url)
        ret = {
            'status': 'error',
            'errors': form.errors.values()[0][0],
            'data': request.POST
        }
        return render(request, tpl_name, ret)
