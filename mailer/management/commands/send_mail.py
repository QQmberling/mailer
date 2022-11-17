import logging

from django.core.management import BaseCommand

from mailer.utils import send_mail

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Send test email.'

    def handle(self, *args, **options):
        to = options['to']
        subject = options['subject']
        data = options['data']
        send_mail(to, 'mail/test_mail.html', subject=subject, context={'data': data})

    def add_arguments(self, p):
        p.add_argument('-t', '--to', type=str, required=True)
        p.add_argument('-s', '--subject', type=str, required=True)
        p.add_argument('-d', '--data', type=str, required=True)
