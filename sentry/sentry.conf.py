# /etc/sentry.conf.py
import os

dbname = os.environ.get('SENTRY_DBNAME', 'sentry')
dbuser = os.environ.get('SENTRY_DBUSER', 'sentry')
dbpass = os.environ.get('SENTRY_DBPASS', 'sentry')
dbhost = os.environ.get('SENTRY_DBHOST', '127.0.0.1')
dbport = os.environ.get('SENTRY_DBPORT', '')
sentry_workers = os.environ.get('SENTRY_WORKERS', 3)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': dbname,
        'USER': dbuser,
        'PASSWORD': dbpass,
        'HOST': dbhost,
        'PORT': dbport,
    }
}

# No trailing slash!
SENTRY_URL_PREFIX = 'http://localhost:7365'

# SENTRY_KEY is a unique randomly generated secret key for your server, and it
# acts as a signing token
SENTRY_KEY = '0123456789abcde'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 7365
SENTRY_WEB_OPTIONS = {
    'workers': int(sentry_workers),  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

ALLOWED_HOSTS = ['localhost', ]
