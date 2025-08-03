#!/bin/bash

# Activar entorno virtual si hace falta (comentado porque Vercel ya instala dependencias)
# source venv311/bin/activate

echo "Ejecutando migraciones..."
python manage.py migrate

echo "Reuniendo archivos estáticos..."
python manage.py collectstatic --noinput

echo "Listo para desplegar 🚀"
