import logging

from django.conf import settings

logger = logging.getLogger(__name__)


INSTALLED_APPS = settings.INSTALLED_APPS + ['anymail']

try:
    from .mailer_local_settings import *
except ImportError:
    logger.info("Unable to import mailer_local_settings.")
    pass
