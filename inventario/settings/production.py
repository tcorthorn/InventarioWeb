from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )


ALLOWED_HOSTS = ['inventarioboran.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5601d5b9m2k2i',
        'USER': 'bmeijvomkhmmhg',
        'PASSWORD': '146ffe81e12d43b90c6babe04422bd3a77a86e1836041ef1751a7f800772adec',
        'HOST': 'ec2-52-72-99-110.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)