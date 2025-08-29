# blog/linkedin_views.py
import requests
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings

# 1. Redirige al usuario a LinkedIn para la autenticación
# Esta es la URL que abrirás en tu navegador para iniciar el proceso
def linkedin_auth(request):
    """
    Constructs the authorization URL and redirects the user to LinkedIn
    to grant permissions to the app.
    """
    client_id = settings.LINKEDIN_CLIENT_ID
    redirect_uri = 'https://django-projects-git-develop-alejandra-martins-projects.vercel.app/linkedin/callback/'
    
    # Scope define los permisos que la aplicación necesita.
    # 'r_liteprofile' es para obtener tu ID de perfil.
    # 'w_member_social' es para poder publicar en tu nombre.
    scope = 'r_liteprofile w_member_social'
        
    # 🕵️‍♀️ Agrega estas dos líneas para depurar
    print(f"DEBUG: El client_id es '{client_id}'")

    auth_url = (f"https://www.linkedin.com/oauth/v2/authorization?"
                f"response_type=code&"
                f"client_id={client_id}&"
                f"redirect_uri={redirect_uri}&"
                f"scope={scope}")
    
    # 🕵️‍♀️ Y esta línea para ver la URL completa
    print(f"DEBUG: La URL de autenticación es: {auth_url}")

    return redirect(auth_url)

# 2. Maneja la respuesta de LinkedIn y obtiene el token de acceso
# LinkedIn redirige a esta vista después de que el usuario da su permiso
def linkedin_callback(request):
    """
    Receives the authorization code from LinkedIn,
    requests an access token, and prints the result.
    """
    client_id = settings.LINKEDIN_CLIENT_ID
    client_secret = settings.LINKEDIN_CLIENT_SECRET
    redirect_uri = 'https://django-projects-git-develop-alejandra-martins-projects.vercel.app/linkedin/callback/'
    code = request.GET.get('code')

    # Si no hay código en la URL, algo salió mal
    if not code:
        return HttpResponse("No se pudo obtener el código de autorización.", status=400)

    # Prepara la petición para intercambiar el código por el token de acceso
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status() # Lanza una excepción si la petición falla
        
        token_data = response.json()
        access_token = token_data.get('access_token')
        expires_in = token_data.get('expires_in')
        
        # Aquí, en un entorno real, guardarías el token de acceso
        # en la base de datos o en un lugar seguro.
        # Por ahora, un simple print sirve para verificar que lo obtuviste.
        print("¡Token de acceso obtenido con éxito!")
        print(f"Token: {access_token}")
        print(f"Expira en: {expires_in} segundos")

        return HttpResponse("Autenticación exitosa. Puedes cerrar esta pestaña.")

    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error al obtener el token: {e}", status=500)