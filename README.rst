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

2. Include the polls URLconf in your project urls.py like this::

    path('mailer/', include('mailer.urls')),

3. Run ``python manage.py migrate`` to create the polls models.
