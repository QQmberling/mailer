=====
Mailer
=====

Mailer is a Django app to send emails via mailjet.

Quick start
-----------

1. Add "mailer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'mailer',
    ]

2. Run ``python manage.py migrate`` to create the message models.
