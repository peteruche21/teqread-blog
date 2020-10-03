from pathlib import Path
from .base import *
from .installed import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
print("using local")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}