#!/usr/bin/env python
# encoding: utf-8

from django import forms
from mongoengine.django.auth import check_password
from .models import BlogUser
from tblog.settings import MONGO_POOL
DB = MONGO_POOL.tblog


class RegisterForm(forms.Form):
    email = forms.CharField(
        label=u'注册邮箱',
        max_length=50,
        widget=forms.TextInput(attrs={'autocomplete': 'off'}),
        error_messages={'required': u'请填写联系人邮箱。'}
    )

    password = forms.CharField(
        label=u'注册密码',
        widget=forms.PasswordInput,
        min_length=8,
        error_messages={
            'required': u'请填写联系人密码。',
            'min_length': u'密码需包含数字和字母，且长度大于8位。'
        }
    )

    def save(self, req_data):
        self.user = BlogUser.create_user(
            req_data['email'],
            req_data['password'],
            req_data['email'],
        )
        self.user.save()
        return self.user


class LoginForm(forms.Form):
    username = forms.EmailField(
        label=u'登录邮箱',
        widget=forms.TextInput,
        required=True,
        )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label=u'登录密码'
        )

    def clean_username(self):
        username = self.data.get('username')
        raw_password = self.data.get('password')
        user = DB.user.find_one({'username': username})
        if not user:
            raise forms.ValidationError(u'用户名或密码错误。')

        user_password = user['password']
        if not check_password(raw_password, user_password):
            raise forms.ValidationError(u'用户名或密码错误。')

        return username
