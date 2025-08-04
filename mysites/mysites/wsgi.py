"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import sys
print("WSGI application starting...", file=sys.stderr)

from django.core.wsgi import get_wsgi_application

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysites.settings')

application = get_wsgi_application()

print("WSGI application loaded", file=sys.stderr)






