from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import TemplateDoesNotExist
from django.conf import settings

from mailer.models import Message


def send_mail(to, template_name, subject, context, **kwargs):
    html_content = render_to_string(template_name, context=context)

    #  It's a good practice to send both html and plain text mails
    try:
        text_content = render_to_string(template_name.replace('.html', '.txt'), context=context)
    except TemplateDoesNotExist:
        text_content = None

    msg = EmailMultiAlternatives(subject, text_content, to=[to], reply_to=[settings.REPLY_TO], **kwargs,)
    msg.attach_alternative(html_content, "text/html")
    # you can set any other options on msg here, then...
    msg.send()
    Message.objects.create(subject=subject)
