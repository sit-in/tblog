# from django.db import models

# from mongoengine.django.auth import User
import datetime
from mongoengine import *
# from mongoengine import StringField, DictField, Document, EmbeddedDocument


class Choice(EmbeddedDocument):
    vote = IntField()


class Blog(Document):
    meta = {'collection': 'blog'}

    title = StringField()
    content = StringField()
    tag = StringField()
    pub_date = DateTimeField(default=datetime.datetime.now)
    choiece = ListField(Choice)
