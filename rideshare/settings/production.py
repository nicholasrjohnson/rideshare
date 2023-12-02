import os
from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False

ALLOWED_HOSTS = ['nicholasrjohnson.com', 'www.nicholasrjohnson.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rideshare',
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True