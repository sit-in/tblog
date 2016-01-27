#!/usr/bin/env python
# encoding: utf-8

from django import forms
from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput,
        required=True,
        error_messages={'required': u'请填写标题'}
    )
    alias_name = forms.SlugField(
        widget=forms.TextInput,
        required=True,
        error_messages={'required': u'请填写标题英文别名'}
    )
    content = forms.CharField(
        widget=forms.TextInput,
        required=True,
        error_messages={'required': u'请填写文章内容'}
    )
    tags = forms.CharField(
        widget=forms.TextInput,
        required=True,
        error_messages={'required': u'请填写文章tag'}
    )

    categories = forms.CharField(
        widget=forms.TextInput,
        required=True,
        error_messages={'required': u'请填写文章分类'}
    )
