#!/usr/bin/env python
# encoding: utf-8

from mongoengine.django.auth import User
from mongoengine import StringField


class BlogUser(User):
    email = StringField(required=True, max_length=50)
    username = StringField(max_length=100)

    USERNAME_FIELD = 'email'

    def __init__(self, *args, **kwargs):
        super(BlogUser, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.email
