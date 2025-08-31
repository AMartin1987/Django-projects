# blog/linkedin_views.py
import requests
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from .models import LinkedInAuthToken # Importa el modelo

# 1. Redirige al usuario a LinkedIn para la autenticación
def linkedin_auth(request):
    """
    Constructs the authorization URL and redirects the user to LinkedIn
    to grant permissions to the app.
    """
    client_id = settings.LINKEDIN_CLIENT_ID
    # Asegúrate de que esta URL sea la de la rama 'develop' de Vercel
    redirect_uri = 'https://django-projects-git-develop-alejandra-martins-projects.vercel.app/linkedin/callback/'
    
    scope = 'r_liteprofile w_member_social'
    
    auth_url = (f"https://www.linkedin.com/oauth/v2/authorization?"
                f"response_type=code&"
                f"client_id={client_id}&"
                f"redirect_uri={redirect_uri}&"
                f"scope={scope}")
    
    return redirect(auth_url)

# 2. Maneja la respuesta de LinkedIn y guarda el token en la base de datos
def linkedin_callback(request):
    """
    Receives the authorization code, requests an access token,
    obtains the profile URN, and saves both to the database.
    """
    client_id = settings.LINKEDIN_CLIENT_ID
    client_secret = settings.LINKEDIN_CLIENT_SECRET
    # Asegúrate de que esta URL sea la de la rama 'develop' de Vercel
    redirect_uri = 'https://django-projects-git-develop-alejandra-martins-projects.vercel.app/linkedin/callback/'
    code = request.GET.get('code')

    if not code:
        return HttpResponse("No se pudo obtener el código de autorización.", status=400)

    # Paso A: Intercambiar el código por el token de acceso
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
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data.get('access_token')
        expires_in = token_data.get('expires_in')

    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error al obtener el token: {e}", status=500)

    # Paso B: Usar el token para obtener el URN del perfil
    me_url = "https://api.linkedin.com/v2/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        me_response = requests.get(me_url, headers=headers)
        me_response.raise_for_status()
        me_data = me_response.json()
        profile_urn = me_data.get('id')
        if profile_urn:
            profile_urn = f"urn:li:person:{profile_urn}"
        else:
            return HttpResponse("No se pudo obtener el URN del perfil de LinkedIn.", status=500)

    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error al obtener el perfil de LinkedIn: {e}", status=500)

    # Paso C: Guardar el token y el URN en la base de datos
    # Si ya existe una entrada, la actualiza; si no, la crea.
    # LinkedInAuthToken.objects.update_or_create(
    #     defaults={'access_token': access_token, 'expires_in': expires_in, 'profile_urn': profile_urn},
    # )
    # LinkedInAuthToken.objects.update_or_create(defaults={
    #     'access_token': access_token,
    #     'expires_in': expires_in,
    #     'profile_urn': profile_urn
    #     })

    try:
        # Busca el token existente o crea uno nuevo si no existe.
        # LinkedInAuthToken.objects.update_or_create(
        #     defaults={'access_token': access_token, 'expires_in': expires_in, 'profile_urn': profile_urn}
        # )

        try:
            # Intenta obtener el primer objeto, ya que solo necesitas uno
            token_obj = LinkedInAuthToken.objects.get()
            token_obj.access_token = access_token
            token_obj.expires_in = expires_in
            token_obj.profile_urn = profile_urn
            token_obj.save()
        except LinkedInAuthToken.DoesNotExist:
            # Si no existe, crea uno nuevo
            LinkedInAuthToken.objects.create(
                access_token=access_token,
                expires_in=expires_in,
                profile_urn=profile_urn
            )

        return HttpResponse("Token de acceso y URN de perfil guardados con éxito. Puedes cerrar esta pestaña.")

    except Exception as e:
        return HttpResponse(f"Error al guardar el token en la base de datos: {e}", status=500)