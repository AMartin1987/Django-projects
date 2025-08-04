import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysites.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def handler(environ, start_response):
    return application(environ, start_response)


