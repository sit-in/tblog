# from django.db import models

# from mongoengine.django.auth import User
import datetime

from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField

from tblog.settings import DOMAIN
from mongo_admin.accounts.models import BlogUser


class Comment(EmbeddedDocument):
    message = StringField(default="DEFAULT EMBEDDED COMMENT")
    author = ReferenceField(BlogUser)


class Article(Document):
    title = StringField(max_length=120, required=True, unique=True)
    alias_name = StringField(max_length=120, unique=True)
    content = StringField(default='I am default content')
    author = ReferenceField(BlogUser, required=True)
    created_date = DateTimeField()
    published_dates = ListField(DateTimeField())
    tags = ListField(StringField(max_length=30))
    category = StringField(max_length=30)
    comments = ListField(EmbeddedDocumentField(Comment))

    def get_absolute_url(self):
        return '%s/%s.html' % (DOMAIN, self.alias_name)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = datetime.datetime.now()
        if self.published_dates:
            self.published_dates.append(datetime.datetime.now())
        super(Article, self).save(*args, **kwargs)


class Page(Document):

    title = StringField(max_length=120, required=True, unique=True)
    content = StringField(default='I am default content')
    url = StringField()
    author = ReferenceField(BlogUser, required=True)
    created_date = DateTimeField()
    published_dates = ListField(DateTimeField())
    comments = ListField(EmbeddedDocumentField(Comment))