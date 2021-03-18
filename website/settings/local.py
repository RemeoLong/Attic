from .base import *

SECRET_KEY = 'rf3=0rzv%q#q=8*qciwfyx9jep99#dyfgb-z)!5l6*^b^sj^^b'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
