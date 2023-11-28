from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ezlr&p##l+4*cufebk&m=@li#qs-=y!o3+*q*k1&nc#)fd=tr1"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = [
    '127.0.0.1',
]





try:
    from .local import *
except ImportError:
    pass
