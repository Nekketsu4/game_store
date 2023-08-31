import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1evy9!=j0a0kzhoc^au$4-*(v9z)8&*4h91u-h7(1k=-pz8z55'


DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_database',
        'USER': 'postgres',
        'PASSWORD': 'GEsUM6NV',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}



STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]