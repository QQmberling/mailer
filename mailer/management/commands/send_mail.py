import json

from django.core.management import BaseCommand

from mailer.core import send_mail


class Command(BaseCommand):

    help = 'Send email.'

    def handle(self, *args, **options):
        to = options['to']
        subject = options['subject']
        context = options['context']
        template_path = options['template_path']
        send_mail(to, template_path, subject=subject, context=context)

    def add_arguments(self, p):
        p.add_argument('-t', '--to', type=str, required=True)
        p.add_argument('-s', '--subject', type=str, required=True)
        p.add_argument('-p', '--template-path', type=str, required=True)
        p.add_argument('-c', '--context', type=json.loads, required=True)
