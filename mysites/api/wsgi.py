"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# Establece la variable de entorno para que Django sepa qué configuración usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# Obtiene la aplicación WSGI de Django
application = get_wsgi_application()

# Añade esta línea para compatibilidad con Vercel
# Vercel busca una variable llamada 'app'
app = application



