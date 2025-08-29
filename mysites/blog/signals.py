# blog/signals.py
import requests
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Post  # Asume que tu modelo se llama Post

@receiver(post_save, sender=Post)
def post_to_linkedin(sender, instance, created, **kwargs):
    """
    Publica automáticamente un enlace en LinkedIn cuando se crea un nuevo post.
    """
    if created:
        # Aquí, necesitas el token de acceso que obtuviste.
        # Por ahora, puedes hardcodearlo temporalmente para la prueba.
        # Luego lo guardarás en la base de datos para acceder a él.
        access_token = "TU_TOKEN_DE_ACCESO_AQUI" 
        
        # Debes obtener tu URN de perfil. Puedes obtenerlo con una llamada a la API de LinkedIn.
        # Para la prueba inicial, puedes hardcodearlo si ya lo tienes.
        # Ejemplo: "urn:li:person:abcdefg"
        author_urn = "TU_URN_DE_PERFIL_O_PAGINA_DE_EMPRESA" 

        linkedin_url = "https://api.linkedin.com/v2/ugcPosts"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }

        # Asegúrate de que tu feed RSS tenga la URL correcta
        blog_post_url = f"https://amartinblog.vercel.app{instance.get_absolute_url()}"
        post_content = {
            "author": author_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": f"Mira mi nuevo post: {instance.title}. {instance.meta_description[:200]}...",
                    "shareMediaCategory": "ARTICLE",
                    "media": [{
                        "status": "READY",
                        "description": {
                            "text": instance.meta_description
                        },
                        "originalUrl": blog_post_url,
                        "title": {
                            "text": instance.title
                        }
                    }]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
            }
        }
        
        try:
            response = requests.post(linkedin_url, headers=headers, data=json.dumps(post_content))
            response.raise_for_status()
            print("Post publicado con éxito en LinkedIn!")
        except requests.exceptions.RequestException as e:
            print(f"Error al publicar en LinkedIn: {e}")