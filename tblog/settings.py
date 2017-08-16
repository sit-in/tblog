# -*- coding: utf-8 -*-

import os
import mongoengine
import pymongo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '2)xd63epwoli9n6=e7e5rfe^42_*j#qg0qma17i^&i6(a*2)qs'

DEBUG = False

# 404 page need debug = False
if DEBUG:
    DOMAIN = 'http://localhost:3000'
else:
    DOMAIN = 'http://blog.ipengtao.com'

DB_NAME = 'tblog'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ipengtao.com', 'www.ipengtao.com']

# mongoengine settings
_MONGODB_HOST = '127.0.0.1:27017'
_MONGODB_NAME = 'tblog'

mongoengine.connect(_MONGODB_NAME, alias='default')

# mongoengine settings
AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'
# mongoengine auth settings
AUTH_USER_MODAL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # must before staticfiles
    'django.contrib.staticfiles',
    'mongoengine.django.mongo_auth',
    'mongo_admin',
    'ui',
    'ui.accounts',
    'markdown_deux',
    'django_jinja',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tblog.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'themes/templates/')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)


WSGI_APPLICATION = 'tblog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
STATIC_URL = '/themes/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "themes/static"),
)

MONGO_POOL = pymongo.mongo_client.MongoClient('localhost', 27017)
