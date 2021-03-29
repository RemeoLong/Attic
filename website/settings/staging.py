from .base import *

SECRET_KEY = '*bb2re7mx&u5xpgml!j734+dv#u((wy^76rkg+tt3cgko3qs-_'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
