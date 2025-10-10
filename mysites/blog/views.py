from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Post
from tracking.models import Visitor
from geoip2.database import Reader

GEOIP_DB_PATH = "api/geo/GeoLite2-City.mmdb"


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def category(request, category_id):
    posts_by_category = Post.objects.filter(category__id=category_id)
    return render(request, "blog/posts_by_category.html", {
        "posts_by_category": posts_by_category,
    })


def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser)
def tracking_simple(request):
    visitas = Visitor.objects.all().order_by('-start_time')[:20]
    total_visitas = Visitor.objects.count()

    geo_info = []
    with Reader(GEOIP_DB_PATH) as reader:
        for v in visitas:
            ip = v.ip_address
            city = country = "Desconocido"
            try:
                response = reader.city(ip)
                city = response.city.name or "Desconocido"
                country = response.country.name or "Desconocido"
            except Exception:
                pass
            geo_info.append({
                "ip": ip,
                "user_agent": v.user_agent,
                "start_time": v.start_time,
                "city": city,
                "country": country
            })

    return render(request, 'blog/tracking_simple.html', {
        'total_visitas': total_visitas,
        'visitas': geo_info
    })