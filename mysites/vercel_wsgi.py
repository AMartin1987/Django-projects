import os
from mysites.wsgi import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysites.settings')

def handler(environ, start_response):
    return application(environ, start_response)

