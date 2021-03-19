import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = ['170.39.76.95', '.atticrestorations.biz', 'ns79.stableserver.net']

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

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_SES_REGION_NAME = 'us-east-2'
AWS_SES_REGION_ENDPOINT ='email.us-east-2.amazonaws.com'
