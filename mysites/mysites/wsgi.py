"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysites.settings')

application = get_wsgi_application()

# BASE_DIR es dos niveles arriba de este archivo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Apuntamos a la carpeta 'static' que está justo en BASE_DIR
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static'))

# ✅ Esto es obligatorio para Vercel
app = application




