# -*- coding: utf-8 -*-

import os
import mongoengine
import pymongo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2)xd63epwoli9n6=e7e5rfe^42_*j#qg0qma17i^&i6(a*2)qs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    DOMAIN = 'http://localhost:3000'
    DB_NAME = 'tblog'
else:
    DOMAIN = 'http://www.ipengtao.com'
    DB_NAME = 'tblog'

ALLOWED_HOSTS = []

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
    'duoshuo',
    'markdown_deux',
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


WSGI_APPLICATION = 'tblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/themes/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "themes/static"),
)

MONGO_POOL = pymongo.mongo_client.MongoClient('localhost', 27017)

DUOSHUO_SECRET = 'de8c773279fae7ee461a8dd1f94bb76c'
DUOSHUO_SHORT_NAME = 'dev-tblog'

# MARKDOWN_DEUX_HELP_URL = "/help/markdown/"
