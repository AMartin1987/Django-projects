import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysites.settings')

from mysites.wsgi import application

def handler(environ, start_response):
    return application(environ, start_response)

import sys
print("WSGI application starting...", file=sys.stderr)
