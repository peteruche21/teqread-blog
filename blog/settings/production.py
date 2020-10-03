import os
from pathlib import Path
from .base import *
from .installed import *

DEBUG = False
ALLOWED_HOSTS = ['*']

print("using production")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

DB_USER_PSW = os.environ.get("DB_USER_PSW")
DB_USER_UN = os.environ.get("DB_USER_UN")
DB_NAME = os.environ.get("DB_NAME", 'production')
INSTANCE_CONNECTION_NAME = os.environ.get("INSTANCE_CONNECTION_NAME")

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER_UN,
        'PASSWORD': DB_USER_PSW,
        'HOST': f'/cloudsql/{INSTANCE_CONNECTION_NAME}',
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = 'Teqqread-Blog <anyaogupeter601@gmail.com>'

ADMINS = (('peter', 'anyaogupeter601@gmail.com'), )
MANAGERS = ADMINS