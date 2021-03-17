import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = ['170.39.76.95',  '.atticrestorations.biz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["DB_name"],
        'USER': os.environ["DB_user"],
        'PASSWORD': os.environ["DB_pass"],
        'HOST': os.environ["DB_host"],
        'PORT': os.environ["DB_port"],
    }
}


