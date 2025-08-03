#!/bin/bash

# Activar entorno virtual si hace falta (comentado porque Vercel ya instala dependencias)
# source venv311/bin/activate

echo "Ejecutando migraciones..."
pip install -r requirements.txt
python manage.py migrate

echo "Reuniendo archivos estáticos..."
python manage.py collectstatic --noinput

echo "Listo para desplegar 🚀"
