# blog/linkedin_urls.py
from django.urls import path
from .templates import linkedin_views

urlpatterns = [
    path('auth/', linkedin_views.linkedin_auth, name='linkedin_auth'),
    path('callback/', linkedin_views.linkedin_callback, name='linkedin_callback'),
]