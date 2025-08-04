#!/bin/bash

# Instala las dependencias
pip install -r requirements.txt

# Recopila los archivos estáticos en la carpeta 'staticfiles'
python3 manage.py collectstatic --noinput