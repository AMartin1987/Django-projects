# blog/feeds.py
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = "Últimos posts de A Martin"
    link = "https://amartinblog.vercel.app/"
    description = "Las últimas entradas del AMartinBlog."

    def items(self):
        # Devuelve las 5 últimas publicaciones.
        return Post.objects.filter(publicado=True).order_by('-fecha_publicacion')[:5]

    def item_title(self, item):
        # Usa el título de la publicación.
        return item.titulo

    def item_description(self, item):
        # Usa el contenido de la publicación. Puedes usar un resumen o el contenido completo.
        return item.contenido[:200]  # Limitar a los primeros 200 caracteres

    def item_link(self, item):
        # Devuelve el enlace a la publicación individual.
        return reverse('post_detail', args=[item.slug])