"""
WSGI config for e_p_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

path = '/Users/Student226123/Desktop/inzynierka/easy-planning/e_p_django'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = DjangoWhiteNoise(get_wsgi_application())
