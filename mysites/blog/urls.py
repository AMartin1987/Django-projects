from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name='post_list'),
    path('posts_by_category/<int:category_id>/', views.category, name='posts_by_category'),
    path('tracking/', views.tracking_simple, name='tracking_simple'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),  # <-- al final
]

