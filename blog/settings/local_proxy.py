from pathlib import Path
from .base import *
from .installed import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

print("using local proxy")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production',
        'USER': 'dbproduser',
        'PASSWORD': "bac74266-c0c8-4d09-ae89-d9c548261cb9",
        'HOST': '127.0.0.1',
        'PORT': '6543',
    }
}