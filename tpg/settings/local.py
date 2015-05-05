from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tpg',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '',
        'PORT': '',
    }
}

