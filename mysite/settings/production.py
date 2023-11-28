import os
from .base import *

DEBUG = False
SECRET_KEY = "8(5v@u1*6)j1o&sgkfy&t%mbkbug47n5*gepugfp+ej8kci2p)",
ALLOWED_HOSTS = ["localhost", "wecleanballoons.com", "*"],

try:
    from .local import *
except ImportError:
    pass

cwd = os.getcwd()
CACHES = {
    "default":{
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "balloons",
        "USER" : "balloons",
        "PASSWORD": "Pepperroni987!",
        "HOST": "LOCALHOST",
        "PORT": "",
    }
}

import sentry_sdk

sentry_sdk.init(
    dsn="https://b9ecbbc8bc4f5c31be5ad9a02faac7ac@o4506304869236736.ingest.sentry.io/4506304871333888",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)