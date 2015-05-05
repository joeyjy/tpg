"""Production settings and globals."""

from os import environ

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'expat',
                'USER': 'ringier',
                'PASSWORD': '1qaz,2wsx',
                'HOST': '172.31.14.105',
                'PORT': '',
        },
}
