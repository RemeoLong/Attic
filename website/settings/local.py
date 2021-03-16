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

# https://docs.djangoproject.com/en/1.6/topics/email/#console-backend

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = 'admin@atticrestorations.biz'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 465
EMAIL_USE_TLS = True

