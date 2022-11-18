from django.conf import settings

INSTALLED_APPS = settings.INSTALLED_APPS + ['anymail']

try:
    from .mailer_local_settings import *
except ImportError:
    print("Unable to find local_settings.py file. Please see README.md for configuration instructions")
    pass
