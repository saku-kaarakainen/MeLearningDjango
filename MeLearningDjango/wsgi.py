"""
WSGI config for MeLearningDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/

WSGI = Web Server Gateway Interface
https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MeLearningDjango.settings')

application = get_wsgi_application()
