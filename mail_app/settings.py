from pathlib import Path

from django.conf import settings


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.SECRET_KEY

DEBUG = settings.DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'anymail',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mail_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mail_app.wsgi.application'

DATABASES = settings.DATABASES

AUTH_PASSWORD_VALIDATORS = settings.AUTH_PASSWORD_VALIDATORS

LANGUAGE_CODE = settings.LANGUAGE_CODE

TIME_ZONE = settings.TIME_ZONE

USE_I18N = settings.USE_I18N

USE_TZ = settings.USE_TZ

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = settings.FROM_EMAIL
REPLY_TO = settings.REPLY_TO
FROM_USER = settings.FROM_USER
EMAIL_BACKEND = settings.EMAIL_BACKEND
ANYMAIL = settings.ANYMAIL
EMAIL_FILE_PATH = settings.EMAIL_FILE_PATH
