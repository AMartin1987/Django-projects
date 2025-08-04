import os

from mysites.wsgi import application

def handler(environ, start_response):
    return application(environ, start_response)

import sys
print("WSGI application starting...", file=sys.stderr)
